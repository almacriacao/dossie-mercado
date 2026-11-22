#!/usr/bin/env python3
"""Gera alma.al/dossiemercado/index.html (estatico, sem rastreador)."""
import json, html

SITE = 'https://alma.al/dossiemercado/'
REEL_URL = 'https://www.instagram.com/alma.prazer/'   # trocar pelo link do Reel quando publicar
CDN = 'https://cdn.jsdelivr.net/gh/almacriacao/dossie-mercado@0f0c7e64ab2714c311338628b5778ee94a470038/'   # arquivos pesados servidos por CDN
PDF = CDN + 'A-engenharia-do-golpe.pdf'
PDF_DL = 'A-engenharia-do-golpe-Alma.pdf'

src = json.load(open('/home/claude/site/sources.json'))
def fix(t):
    t = t.split('Checado em')[0].rstrip()
    return t.replace('Decreto- Lei', 'Decreto-Lei').replace('- ', '-') if 'Decreto' in t else t
items = []
for e in src:
    parts = []
    for p in e['parts']:
        t = html.escape(fix(p['text']))
        if p.get('url'):
            parts.append(f'<a href="{html.escape(p["url"])}" target="_blank" rel="noopener">{t}</a>')
        else:
            parts.append(t)
    body = ' '.join(parts).replace(' · ', ' · ')
    items.append(f'<li><b>{html.escape(e["label"])}</b> {body}</li>')
SOURCES = '\n'.join(items)
NLINKS = sum(1 for e in src for p in e['parts'] if p.get('url'))

L = {
 'mt': 'https://www.moneytimes.com.br/ibovespa-26-10-26-lils/',
 'rk': 'https://rankia.com.br/ibovespa-cai-13-88-dolar-dispara-reeleicao-lula-circuit-breaker/',
 'fb': 'https://forbes.com.br/forbes-money/2026/08/fortuna-bilionarios-brasileiros-r-186-trilhao-pib/',
 'jb': 'https://jornaldebrasilia.com.br/noticias/politica-e-poder/lula-sanciona-orcamento-de-2026-e-veta-quase-r-400-milhoes-em-emendas/',
 'bc': 'https://www.bcb.gov.br/content/estatisticas/hist_estatisticasfiscais/202601_Texto_de_estatisticas_fiscais.pdf',
 'ag': 'https://agenciagov.ebc.com.br/noticias/202504/presidente-sanciona-a-lei-orcamentaria-anual-de-2025-com-vetos-pontuais',
 'rot': 'https://viva.com.br/dinheiro/endividamento-das-familias-sobe-a-501-em-agosto-novo-recorde-da-serie.html',
 'tc': 'https://istoedinheiro.com.br/bc-firma-centesimo-termo-de-compromisso-com-entidade-supervisionada',
 'itau': 'https://www.infomoney.com.br/mercados/itau-itub4-resultados-quarto-trimestre-2025/',
 'met': 'https://www.metropoles.com/brasil/camara-votacao-regulamentacao-reforma-tributaria',
 'ec': 'https://www12.senado.leg.br/ecidadania/visualizacaomateria?id=137929',
}

SHARE_TXT = 'A engenharia do golpe: como os bilionários transformam uma derrota nas urnas em lucro. E como a gente dá o troco. Dossiê grátis da Alma:'

tpl = open('/home/claude/site/template.html').read()
out = (tpl.replace('{{SOURCES}}', SOURCES).replace('{{NLINKS}}', str(NLINKS))
          .replace('{{REEL}}', REEL_URL).replace('{{PDF}}', PDF).replace('{{PDF_DL}}', PDF_DL)
          .replace('{{SITE}}', SITE).replace('{{CDN}}', CDN).replace('{{SHARE_TXT}}', html.escape(SHARE_TXT)))
for k, v in L.items():
    out = out.replace('{{L:' + k + '}}', html.escape(v))
assert '{{' not in out, out[out.index('{{'):out.index('{{') + 40]
assert '—' not in out and '–' not in out, 'travessao no texto'
open('/home/claude/site/dossiemercado/index.html', 'w').write(out)
print('ok', len(out), 'links', NLINKS)
