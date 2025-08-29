<h1>TwitchToSpeach</h1>
This is a simple python app inspired by Doug Doug's ChatGodApp. It uses Azure TTS to read out Twitch chat messages. Chatters can use different emotions by using keywords in asterisk, and different voices by using keywords in Parenthesis.
<h2>Setup</h2>
<ul>
  <li>Run "pip install -r dependencies.txt"</li>
  <li>Get a token at dev.twitch.tv or twitchtokengenerator.com</li>
  <li>Make a windows environment variable with the name "TWITCH_ACCESS_TOKEN" and the value set to your token</li>
  <li>Sign up for Microsoft Azure, create a TTS resource, and get your acces key and region</li>
  <li>Make windows environment variables "AZURE_TTS_KEY" and "AZURE_TTS_REGION" and set them to their respective values</li>
  <li>Run "TwitchToSpeach.py" and everything should be good to go</li>
</ul>
<h2>Keywords</h2>
<h3>Emotions (Styles)</h3>
<ul>
  <li>*whispers*</li>
  <li>*whispering*</li>
  <li>*whisper*</li>
  <li>*shouting*</li>
  <li>*shouts*</li>
  <li>*shout*</li>
  <li>*rudely*</li>
  <li>*unfriendly*</li>
  <li>*scared*</li>
  <li>*afraid*</li>
  <li>*horrified*</li>
  <li>*terrified*</li>
  <li>*saddened*</li>
  <li>*sorrowful*</li>
  <li>*depressingly*</li>
  <li>*depressed*</li>
  <li>*sadly*</li>
  <li>*sad*</li>
  <li>*regularly*</li>
  <li>*regular*</li>
  <li>*default*</li>
  <li>*normally*</li>
  <li>*normal*</li>
  <li>*hopefully*</li>
  <li>*hopeful*</li>
  <li>*ecstatically*</li>
  <li>*ecstatic*</li>
  <li>*excitedly*</li>
  <li>*excited*</li>
  <li>*joyfully*</li>
  <li>*joyful*</li>
  <li>*happy*</li>
  <li>*happily*</li>
  <li>*cheerfully*</li>
  <li>*cheerful*</li>
  <li>*furiously*</li>
  <li>*furious*</li>
  <li>*angered*</li>
  <li>*angrily*</li>
  <li>*angry*</li>
</ul>
<h3>Voices</h3>
<ul>
  <li>(davis)</li>
  <li>(tony)</li>
  <li>(jason)</li>
  <li>(guy)</li>
  <li>(jane)</li>
  <li>(nancy)</li>
  <li>(jenny)</li>
  <li>(aria)</li>
  <li>(sara)</li>
  <li>(girl)</li>
  <li>(masculine)</li>
  <li>(feminine)</li>
  <li>(fem)</li>
  <li>(masc)</li>
  <li>(default)</li>
  <li>(regular)</li>
  
</ul>
