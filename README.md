# Propuesta Constitución Política en formato JSON

**Aún falta un poco de trabajo**

Este repositorio contiene un pequeño script en python que utilice para leer el archivo pdf de la propuesta y transformarlo a un formato json.

Un ejemplo de la estructura:

```json
[
    {
        "title": "Capítulo I Principios y Disposiciones Generales",
        "page": 9,
        "articles": [
            {
                "title": "Artículo 1",
                "sections": [
                    {
                        "number": 1,
                        "content": "1. Chile es un Estado social y democrático de derecho. Es plurinacional, intercultural, regional y ecológico.",
                        "subsections": []
                    },
                    {
                        "number": 1,
                        "content": "2. Se constituye como una república solidaria. Su democracia es inclusiva y paritaria. Reconoce como valores intrínsecos e irrenunciables la dignidad, la libertad, la igualdad sustantiva de los seres humanos y su relación indisoluble con la naturaleza.",
                        "subsections": []
                    },
                    {
                        "number": 1,
                        "content": "3. La protección y garantía de los derechos humanos individuales y colectivos son el fundamento del Estado y orientan toda su actividad. Es deber del Estado generar las condiciones necesarias y proveer los bienes y servicios para asegurar el igual goce de los derechos y la integración de las personas en la vida política, económica, social y cultural para su pleno desarrollo.",
                        "subsections": []
                    }
                ]
            }
        ]
    }
]
```
