Canonical page: https://digit-video.luopeike.com/pt-BR/help

Dig It

# Ajuda e suporte do Dig It

Conheça os lotes no Mac, revisão de quadros, folhas de contato, projetos salvos e diferenças entre plataformas do Dig It, além da disponibilidade da CLI.

[App Store](https://apps.apple.com/app/id6508171056)

## O que muda entre Mac, iPhone e iPad?

### Mac

O Mac acrescenta fila em lote, importação de pastas, predefinições, exportação automática PNG/JPEG e revisão de quadros próximos da fonte. Escolha uma pasta de saída antes de ativar a exportação automática.

### iPhone / iPad

No iPhone e iPad, escolha um vídeo em Fotos ou Arquivos, revise as imagens, exporte PNGs selecionados ou uma folha de contato e salve os resultados no Histórico.

## Primeiros passos

1. Escolha Equilibrado, Capa ou Passos.

2. Importe um vídeo de Arquivos ou Fotos.

3. Revise os quadros extraídos e selecione os que deseja manter.

4. Exporte PNGs selecionados ou salve o projeto no histórico.

## Escolher um modo de extração

- Equilibrado: conjunto médio e limpo para a maioria dos vídeos.

- Capa: menos quadros, mais fortes, para miniaturas e capas.

- Passos: mais pontos de mudança para tutoriais e fluxos de trabalho.

## Fluxos práticos para quadros de vídeo

[Extrair quadros de vídeo em lote no Mac Adicione vídeos ou uma pasta, escolha uma predefinição e revise cada resultado ou exporte PNG/JPEG automaticamente. Todo o processamento acontece no Mac. Ler o guia →](https://digit-video.luopeike.com/pt-BR/batch-extract-video-frames-on-mac)

[Criar uma folha de contato de vídeo Uma folha de contato reúne imagens de vídeo em uma visão geral PNG. Compare capas, compartilhe um resumo de cenas ou junte etapas de tutorial sem enviar o vídeo original. Ler o guia →](https://digit-video.luopeike.com/pt-BR/video-contact-sheet)

## Extraia quadros por intervalo ou tempo no Mac

As novidades exigem a versão 1.4.3 ou posterior. Se a atualização ainda não estiver na sua App Store, você pode continuar usando as opções anteriores de exportação.

Antes de adicionar vídeos ao espaço do Mac, escolha quadros-chave automáticos, intervalo fixo, tempos específicos ou distribuição uniforme e um limite de 1–120 quadros. O intervalo fixo para no limite; a distribuição uniforme cobre todo o vídeo. Os tempos aceitam segundos ou HH:MM:SS, por exemplo 5, 00:12.5, 01:30. Ative Resolução original para exportação automática ou selecione resultados e use Exportar → Exportar na resolução original → PNG/JPEG. Os originais são decodificados e salvos um por vez, sem ampliação. A saída 4K exige uma fonte 4K e o vídeo original deve permanecer disponível no espaço de trabalho.

## Exporte capas e folhas de contato PDF para impressão

No Mac, iPhone ou iPad, selecione um resultado e use Exportar → Exportar capa. Escolha proporção original, 16:9, 9:16, 1:1 ou 4:3, ajuste o corte e o lado máximo e salve PNG/JPEG. O JPEG pode ter limite de 2 MB; reduza as dimensões se não couber. As imagens não são ampliadas. Para uma folha PDF, escolha A4/Letter e 2–4 colunas. Até 120 quadros são ordenados cronologicamente e paginados com nome do vídeo e tempos. Sem seleção, todos os resultados restantes são usados. A folha PNG continua limitada a 40 quadros.

## Escolha uma imagem entre quadros próximos da fonte

No Mac, selecione um resultado, percorra quadros próximos da fonte e adicione uma imagem ou substitua a selecionada. O vídeo original precisa continuar disponível no espaço de trabalho atual.

[![Resultados do Mac e revisão da fonte com um vídeo de exemplo. Interface em inglês.](https://digit-video.luopeike.com/images/mac-frame-review.webp)](https://digit-video.luopeike.com/images/mac-frame-review.webp)

Resultados do Mac e revisão da fonte com um vídeo de exemplo. Interface em inglês.

Vídeo de exemplo: Big Buck Bunny. © 2008 Blender Foundation. Quadros organizados com Dig It. [Big Buck Bunny](https://peach.blender.org/about/) · [CC BY 3.0](https://creativecommons.org/licenses/by/3.0/)

## Salve um conjunto de quadros para editar novamente

Salvar mantém as imagens atuais e os tempos e pontuações disponíveis no Histórico local. Reabra um projeto para revisar, excluir, exportar e salvar alterações no mesmo registro. O vídeo original não é armazenado; registros antigos apenas com metadados não podem recriar imagens ausentes.

## Folhas PNG: até 40 quadros

Uma folha PNG aceita até 40 quadros. Para uma visão maior para impressão, escolha PDF: até 120 quadros com paginação automática. O espaço do Mac também exporta folhas PNG e PDF.

## Perguntas frequentes

### O Dig It envia meus vídeos para a internet?

Não. Análise e extração acontecem no dispositivo. Você escolhe compartilhar arquivos exportados; a extração local não precisa de internet.

### Preciso do FFmpeg?

Não. O app da App Store usa os frameworks locais de vídeo da Apple. O fluxo gráfico não exige comandos do Terminal nem instalação separada do FFmpeg.

### O Dig It é gratuito?

O Dig It é atualmente gratuito na App Store. Consulte o link oficial para preço e compatibilidade atualizados.

### O Histórico guarda meu vídeo original?

Não. Guarda as imagens salvas explicitamente e seus metadados, não o vídeo original. A revisão da fonte no Mac exige um vídeo disponível no espaço de trabalho atual.

### Todas as imagens mantêm a resolução original?

As prévias cabem em 720 × 720 pixels. A exportação original no Mac decodifica o vídeo sob demanda e mantém suas dimensões. Capas no Mac usam a fonte disponível ou a resolução da imagem salva. Imagens de baixa resolução não são ampliadas.

### A CLI vem no download da App Store?

Não. digit é uma ferramenta separada para Mac e ainda não tem download público. Consulte o suporte antes de usar os exemplos. A integração MCP não está disponível.

### Why does it ask for Photos access?

Dig It uses Photos access only so you can choose source media and save exported results when you ask it to.

## Ferramentas opcionais de linha de comando para Mac

A CLI digit é separada do app da App Store e ainda não é distribuída publicamente. Consulte o suporte sobre acesso. Os exemplos abaixo são para quem já instalou a ferramenta independente.
[Consultar o suporte sobre a CLI](https://digit-video.luopeike.com/pt-BR/support)

```sh
digit extract video.mp4 --output ./frames --mode balanced --json frames.json
```

```sh
digit contact-sheet video.mp4 --output sheet.png --columns 4 --limit 40
```

```sh
digit sample video.mp4 --output ./samples --every 10 --max 30 --json samples.json
```

```sh
digit extract video.mp4 --output ./originals --resolution source --json originals.json
```

```sh
digit preset-template --output workflow.json
```

```sh
digit extract video.mp4 --output ./frames --preset workflow.json
```
