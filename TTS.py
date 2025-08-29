import os
import azure.cognitiveservices.speech as speechsdk

#Set key and region environment variables
speech_config = speechsdk.SpeechConfig(subscription=os.environ.get('AZURE_TTS_KEY'), region=os.environ.get('AZURE_TTS_REGION'))
#audio config
audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True)
speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)

def speak(text = 'Error 404: Text missing', style = 'hopeful', voice = 'en-US-DavisNeural'):
    #SSML
    speech_synthesis_voice_name = voice
    ssml = f"""<speak version='1.0' xml:lang='en-US' xmlns='http://www.w3.org/2001/10/synthesis' xmlns:mstts='http://www.w3.org/2001/mstts'>
    <voice name="{{}}">
        <mstts:express-as style="{style}">
        {text}
        </mstts:express-as>
    </voice>
</speak>""".format(speech_synthesis_voice_name)
    
    #Synthesize the SSML
    speech_synthesis_result = speech_synthesizer.speak_ssml_async(ssml).get()

#Handle Errors
    if speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = speech_synthesis_result.cancellation_details
        print("Speech synthesis canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            if cancellation_details.error_details:
                print("Error details: {}".format(cancellation_details.error_details))
                print("Did you set the speech resource key and region values?")