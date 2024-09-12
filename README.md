# OVOS Wav2Vec STT

## Description

OVOS plugin for [Wav2Vec](https://ai.meta.com/blog/wav2vec-20-learning-the-structure-of-speech-from-raw-audio/)

## Install

`pip install ovos-stt-plugin-wav2vec`

## Configuration

```json
  "stt": {
    "module": "ovos-stt-plugin-wav2vec",
    "ovos-stt-plugin-wav2vec": {
        "model": "proxectonos/Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm"
    }
  }
```

`"model"` can be any compatible wav2vec model from hugging face, if not set, it will be automatically selected based on language

### Models

Supported languages: `'gl'`

- `"proxectonos/Nos_ASR-wav2vec2-large-xlsr-53-gl-with-lm"` (default)
- `"diego-fustes/wav2vec2-large-xlsr-gl"`

## Credits

<img src="img.png" width="128"/>

> This plugin was funded by the Ministerio para la Transformación Digital y de la Función Pública and Plan de Recuperación, Transformación y Resiliencia - Funded by EU – NextGenerationEU within the framework of the project ILENIA with reference 2022/TL22/00215337

<img src="img_1.png" width="64"/>

> O [Proxecto Nós](https://github.com/proxectonos) é un proxecto da Xunta de Galicia cuxa execución foi encomendada á Universidade de Santiago de Compostela, a través de dúas entidades punteiras de investigación en intelixencia artificial e tecnoloxías da linguaxe: o ILG (Instituto da Lingua Galega) e o CiTIUS (Centro Singular de Investigación en Tecnoloxías Intelixentes).