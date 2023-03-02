###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_cores = []
caminho = 'C:\\Users\\Lipe\Documents\\100 Days of Code The Complete Python Pro Bootcamp for 2023\\day_18\\pintura_de_pontos\\day_18.jpg'
cores = colorgram.extract(caminho, 50)

# Com esse laço eu gero uma paleta de cores de acordo com as cores identicadas
# na imagem escolhida. 
for cor in cores:
    vermelho = cor.rgb.r #pega o rgb da cor vermelha
    verde = cor.rgb.g #pega o rgb da verde
    azul = cor.rgb.b #pega o rgb da cor azul
    nova_cor = (vermelho,verde,azul)
    rgb_cores.append(nova_cor)




