import os
from dotenv import load_dotenv, dotenv_values
import azure.cognitiveservices.speech as speechsdk

def speak_to_microphone(api_key, region, output_file):
    speech_config = speechsdk.SpeechConfig(subscription=api_key, region=region)
    speech_config.speech_recognition_language = "en-US"
    audio_config = speechsdk.audio.AudioConfig(device_name='{0.0.1.00000000}.{520CFE79-9C92-4049-8C4C-7B22ABFFEB90}')
    speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_InitialSilenceTimeoutMs, "60000") # 60 seconds
    speech_recognizer.properties.set_property(speechsdk.PropertyId.SpeechServiceConnection_EndSilenceTimeoutMs, "20000") # 20 seconds

    print("Speak into your microphone")

    with open(output_file, "w") as file:
        while True:
            speech_recognition_result = speech_recognizer.recognize_once_async().get()

            if speech_recognition_result.reason == speechsdk.ResultReason.RecognizedSpeech:
                print("{}".format(speech_recognition_result.text))
                file.write("{}\n".format(speech_recognition_result.text))
                if "stop session" in speech_recognition_result.text.lower():
                    print("Session ended by user.")
                    break
            elif speech_recognition_result.reason == speechsdk.ResultReason.NoMatch:
                print("No speech could be recognized: {}".format(speech_recognition_result.no_match_details))
            elif speech_recognition_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_recognition_result.cancellation_details
                print("Speech recognition canceled: {}".format(cancellation_details.reason))
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    print("Error details: {}".format(cancellation_details.error_details))
                    print("Did you set the speech resource key and region values?")
load_dotenv()

api_key = os.getenv("api_key")
region = os.getenv("region")
output_file = "recognized_speech.txt"

speak_to_microphone(api_key, region, output_file)
