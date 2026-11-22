# Fonte da página alma.al/dossiemercado

- `template.html`: a página, com marcadores `{{...}}`.
- `build.py`: monta o `index.html` (troca os marcadores, confere que não tem travessão). Endereço da CDN fica na variável `CDN`.
- `sources.json`: as fontes do dossiê (lista no fim da página).
- `og.html`: a arte do cartão de compartilhamento (og.jpg).
- `htaccess.txt`: cópia do `.htaccess` que está no servidor (cache, compressão e redirecionamento do PDF).

O `build.py` espera estes arquivos em `/home/claude/site/`. Pra rodar em outro lugar, ajuste os caminhos no começo do script.
