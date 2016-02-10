#DECLARACIONES DE ESCENARIOS.
#Primero, las imagenes de un color.
image black_screen = "img/bg/bg_blackscreen.jpg" #pantalla negra
image white_screen = "img/bg/bg_whitescreen.png" #pantalla blanca


#AQUI VAN SUS SIGLAS: TIPO_ESCENA_ESTADO
#BG TYPE: D-DÍA N-NOCHE G-GRIS SS-ATARDECER ALT-ALTERNATIVO
#Habitación:
image room_day = "img/bg/bg_room_d.png"
#Sala de estar
image sala_day = "img/bg/bg_sala_d.png"
#afuera de la casa
image afuerame_day = "img/bg/bg_houseout_d.png"
image afuerame_nalt = "img/bg/bg_houseout_nalt.png"

# PERSONAJES Y SUS CÓDIGOS.

define gou = Character('Tachibana Gou', color="#c8ffc8")
define me = Character('Sutefan', color="#c8ffc8")
define idk = Character('????', color="#c8ffc8")
define voz = Character('Voz', color="#c8ffc8")
define dev = Character('Nakurusa', color="#c8ffc8")

#SPRITES PERSONAJES
#POR CATEGORÍA OBVIO JEJEJEJEJEJ
#
#GOU EXPRESIONES - ESCOLAR
image gou_puchero = "img/spr/spr_gou_puch.png"
image gou_normal = "img/spr/spr_gou_normal.png"


label start:
#INTRODUCCION#

    scene black_screen
    play sound "sounds/birds.wav" loop
    idk "¿Qué esperas? ¡Ven a sentarte! Deja de estar molestando..."
    voz "¡Perdón! Voy enseguida"
    idk "Vamos, debes comer para crecer fuerte..."
    voz "Está bien..."
    "..."
    scene room_day
    with fade
    play sound "sounds/roukadash.wav"
    "...Llegu-"
    "Oh..."
    me "Sólo fue un sueño..."
    play sound "sounds/roukadash.wav"
    "..."
    play sound "sounds/roukadash.wav"
    "..¿Están tocando la puerta?"
    play sound "sounds/roukadash.wav"
    idk "¡Primoo!~ Abreme la puerta, estoy aquí afuera hace diez minutos y aún no la abres... No deberías ponerle pestillo a la puerta, idiota."
    "Oh demonios, casi se me olvida, ¡hoy es el primer día de escuela! ..."
    "Bueno para mí, ya que llegue tarde a la escuela por unos problemas..."
    play sound "sounds/roukadash.wav"
    me "Vooy, voy..."
    voz "¡Apresúrate!"
    play music "bgm/Fertilizer.mp3" fadein 1.0
    me "¿Qué sucede, Gou?"
    show gou_puchero
    with dissolve
    gou "¿¡Cómo que qué sucede!? ¿Acaso no te das cuenta la hora que es? Mira, son las 7:30 AM... Ya casi es hora de ir a la escuela. Vístete luego, tu uniforme está en el armario."
    hide gou_puchero
    with dissolve
    "¿Desde cuándo que Gou es así de responsable? Me parece un poco tierno que se preocupe de esa manera de mí."
    me "Está bien, está bien, me cambiaré de ropa lo más rápido posible. Tendré que saltarme el desayú-"
    show gou_puchero
    with dissolve
    gou "¡ESO NUNCA! Debes comer bien ¡sobre todo tu desayúno! Baja ahora mismo y come o me enojaré contigo... Idiota."
    "¡Qué adorable!"
    me "Bien, bien, bajaré..."
    hide gou_puchero
    with dissolve
    stop music fadeout 2.0
    scene afuerame_day
    with fade
    play music "bgm/laotraxd.mp3" fadein 1.0
    me "Bueno, guíame hacía la escuela Gou..."
    show gou_normal
    with dissolve
    gou "Perfecto~ Sigueme primo, no es tan largo el camino."
    me "Vamos, vamos..."
    "Espero que no se entere que ya son las 8:00 am... Se volverá loquisima..."
    stop music
    idk "..."
    idk "¿Qué te crees...?"
    me " ¿¡Quén eres!?"
    hide gou_normal
    with dissolve
    scene afuerame_nalt
    play music "bgm/what.mp3"
    idk "Debes saber algo, amigo...."
    idk "En este mundo...."
    idk "...." 
    idk "ES ASESINAR O SER ASESINADO..."
    dev "Ese fue un regalo pal gonchi que cada 3 segundos dice la misma wea..."
    dev "Perdón si el dialogo fue super penca, pero lo hice para probar las capacidades del programa"
    dev "Cuando me ponga en serio cambiará toda esta parte, de hecho se supone que estaría la mamá en esta escena..."
    dev "Pero bueno, para que sepan que estamos comenzando, panitas."
    dev "Los camo cabros, suerte con las chicas :$"
    dev "PRONTO, MAS LOLICON Y SEXO, MARTIN TUTORIAL Y GONCHI LOLI SEXUALIZADA"
    dev "DIEGITO YANDERE, JUAKO LA PERKINAZA, CHINITO LA FRÍA Y NAKURUSA LA DEPRESIVA"
    dev "Todo eso y más en...."
    dev "LOS PANITAS SCHOOL, NOVELA VISUAL!"


    return
