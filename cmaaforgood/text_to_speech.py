"""
Note: ssml must be well-formed according to:
    https://www.w3.org/TR/speech-synthesis/
"""
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=os.getcwd() + '/config.json'
from google.cloud import texttospeech

form_questions = ['Agency Name',
'Project Name',
'Participant Last Name',
'Participant First Name',
'Participant Middle Initial',
'Address Number',
'Address Direction',
'Address Street Name',
'Address Apartment Number',
'Type of Program',
'Telephone Number',
'Zip Code ',
'Is the participant a homeless youth?',
'Ethnicity',
'Race',
'Gender', 
'Age',
'Birth date',
'Current Grade (If in school) or Highest Level of Education Completed',
'School',
'Is the participant disabled?',
'If you answered yes to the previous question, please specify',
'Community Area',
'Ward',
'Family Type',
'Housing Status',
'Food Stamps?',
'Free/Reduced Lunch?',
'Health Insurance?',
'Income Source (Check all that apply)',
'Source of Referral',
'Client ID']

# Instantiates a client
client = texttospeech.TextToSpeechClient()

i = 0
for i in range(len(form_questions)):
        # Set the text input to be synthesized
        synthesis_input = texttospeech.types.SynthesisInput(text=form_questions[i])

        # Build the voice request, select the language code ("en-US") and the ssml
        # voice gender ("neutral")
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='es-ES',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.NEUTRAL)

        # Select the type of audio file you want returned
        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        # Perform the text-to-speech request on the text input with the selected
        # voice parameters and audio file type
        response = client.synthesize_speech(synthesis_input, voice, audio_config)

        # The response's audio_content is binary.
        with open('Assets/audio/question_'+str(i)+'.mp3', 'wb') as out:
            # Write the response to the output file.
            out.write(response.audio_content)
            print('Audio content written to file "output'+str(i)+'.mp3"')
