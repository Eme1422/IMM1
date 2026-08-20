import streamlit as st
import os
import time
import glob
import os
from gtts import gTTS
from PIL import Image
import base64

st.title("Conversión de Texto a Audio")
image = Image.open('gato_raton.png')
st.image(image, width=350)
with st.sidebar:
    st.subheader("Esrcibe y/o selecciona texto para ser escuchado.")


try:
    os.mkdir("temp")
except:
    pass

st.subheader("Una pequeña Fábula.")
st.write('Había una vez un príncipe que quería casarse con una princesa pero con una verdadera princesa de sangre real. Viajó por todo el mundo buscando una, pero era muy difícil encontrarla, mucho más difícil de lo que había supuesto.   Las princesas abundaban, pero no era sencillo averiguar si eran de sangre real. Siempre acababa descubriendo en ellas algo que le demostraba que en realidad no lo eran, y el príncipe volvió a su país muy triste por no haber encontrado una verdadera princesa real.
   Una noche, estando en su castillo, se desencadenó una terrible tormenta: llovía muchísimo, los relámpagos iluminaban el cielo y los truenos sonaban muy fuerte. De pronto, se oyó que alguien llamaba a la puerta:
   -¡ Toc, toc!
   La familia no entendía quién podía estar a la intemperie en semejante noche de tormenta y fueron a abrir la puerta.
   -¿ Quién es? - preguntó el padre del príncipe.
   - Soy la princesa del reino de Safi - contestó una voz débil y cansada. - Me he perdido en la oscuridad y no sé regresar a donde estaba.
   Le abrieron la puerta y se encontraron con una hermosa joven:
   - Pero ¡Dios mío! ¡Qué aspecto tienes!
   La lluvia chorreaba por sus ropas y cabellos. El agua salía de sus zapatos como si de una fuente se tratase. Tenía frío y tiritaba.
   En el castillo le dieron ropa seca y la invitaron a cenar. Poco a poco entró en calor al lado de la chimenea.
   La reina quería averiguar si la joven era una princesa de verdad.
   "Ya sé lo que haré - pensó -. Colocaré un guisante debajo de los muchos edredones y colchones que hay en la cama para ver si lo nota. Si no se da cuenta no será una verdadera princesa. Así podremos demostrar su sensibilidad".
   Al llegar la noche, la reina colocó un guisante bajo los colchones y después se fue a dormir.
   A la mañana siguiente, el príncipe preguntó:
   -¿Qué tal has dormido, joven princesa?
   - ¡Oh! Terriblemente mal - contestó -. No he dormido en toda la noche. No comprendo qué tenía la cama; Dios sabe lo que sería. Tengo el cuerpo lleno de cardenales. ¡Ha sido horrible!
   - Entonces, ¡eres una verdadera princesa! Porque a pesar de los muchos colchones y edredones, has sentido la molestia del guisante. ¡Sólo una verdadera princesa podía ser tan sensible!
   El príncipe se casó con ella porque estaba seguro de que era una verdadera princesa. Después de tanto tiempo, al final encontró lo que quería.
   Y colorín colorado, este cuento se ha acabado'
        
        )
           
st.markdown(f"Quieres escucharlo?, copia el texto")
text = st.text_area("Ingrese El texto a escuchar.")

tld='com'
option_lang = st.selectbox(
    "Selecciona el lenguaje",
    ("Español", "English"))
if option_lang=="Español" :
    lg='es'
if option_lang=="English" :
    lg='en'

def text_to_speech(text, tld,lg):
    
    tts = gTTS(text,lang=lg) # tts = gTTS(text,'en', tld, slow=False)
    try:
        my_file_name = text[0:20]
    except:
        my_file_name = "audio"
    tts.save(f"temp/{my_file_name}.mp3")
    return my_file_name, text


#display_output_text = st.checkbox("Verifica el texto")

if st.button("convertir a Audio"):
     result, output_text = text_to_speech(text, 'com',lg)#'tld
     audio_file = open(f"temp/{result}.mp3", "rb")
     audio_bytes = audio_file.read()
     st.markdown(f"## Tú audio:")
     st.audio(audio_bytes, format="audio/mp3", start_time=0)

     #if display_output_text:
     
     #st.write(f" {output_text}")
    
#if st.button("ElevenLAabs",key=2):
#     from elevenlabs import play
#     from elevenlabs.client import ElevenLabs
#     client = ElevenLabs(api_key="a71bb432d643bbf80986c0cf0970d91a", # Defaults to ELEVEN_API_KEY)
#     audio = client.generate(text=f" {output_text}",voice="Rachel",model="eleven_multilingual_v1")
#     audio_file = open(f"temp/{audio}.mp3", "rb")

     with open(f"temp/{result}.mp3", "rb") as f:
         data = f.read()

     def get_binary_file_downloader_html(bin_file, file_label='File'):
        bin_str = base64.b64encode(data).decode()
        href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
        return href
     st.markdown(get_binary_file_downloader_html("audio.mp3", file_label="Audio File"), unsafe_allow_html=True)

def remove_files(n):
    mp3_files = glob.glob("temp/*mp3")
    if len(mp3_files) != 0:
        now = time.time()
        n_days = n * 86400
        for f in mp3_files:
            if os.stat(f).st_mtime < now - n_days:
                os.remove(f)
                print("Deleted ", f)


remove_files(7)
