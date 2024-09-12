from tempfile import NamedTemporaryFile
from typing import Optional

import torch
import torchaudio
from ovos_plugin_manager.templates.stt import STT
from speech_recognition import AudioData
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

LANG2MODEL = {
    "gl": "proxectonos/Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm"
}


class Wav2VecSTT(STT):

    def __init__(self, config: dict = None):
        super().__init__(config)
        model = self.config.get("model")
        lang = self.lang.split("-")[0]
        if not model and lang in LANG2MODEL:
            model = LANG2MODEL[lang]
        if not model:
            raise ValueError(f"'lang' {lang} not supported, a 'model' needs to be explicitly set in config file")
        self.processor = Wav2Vec2Processor.from_pretrained(model)
        self.asr_model = Wav2Vec2ForCTC.from_pretrained(model)

    @property
    def available_languages(self) -> set:
        return set(LANG2MODEL.keys())

    def transcribe_file(self, file_path: str) -> str:
        waveform, sample_rate = torchaudio.load(file_path)
        # Resample if the audio is not at 16kHz
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(sample_rate, 16000)
            waveform = resampler(waveform)
        inputs = self.processor(waveform.squeeze().numpy(), sampling_rate=16_000, return_tensors="pt", padding=True)
        with torch.no_grad():
            logits = self.asr_model(inputs.input_values, attention_mask=inputs.attention_mask).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        return self.processor.batch_decode(predicted_ids)[0]

    def execute(self, audio: AudioData, language: Optional[str] = None):
        language = language or self.lang
        if language.split("-")[0] not in self.available_languages:
            raise ValueError(f"'lang' {language} not supported")
        with NamedTemporaryFile("wb", suffix=".wav") as f:
            f.write(audio.get_wav_data())
            transcription = self.transcribe_file(f.name)
        return transcription


if __name__ == "__main__":
    b = Wav2VecSTT({"lang": "gl"})
    from speech_recognition import Recognizer, AudioFile

    eu = "/home/miro/PycharmProjects/ovos-stt-wav2vec-plugin/9ooDUDs5.wav"
    with AudioFile(eu) as source:
        audio = Recognizer().record(source)

    a = b.execute(audio, language="gl")
    print(a)
    # ten en conta que as funcionarlidades incluídas nesta páxino ofrécense unicamente con fins de demostración se tes algún comentario subxestión ou detectas algún problema durante a demostración ponte en contacto con nosco

