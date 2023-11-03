from abc import ABC, abstractmethod
if __name__ != "__main__":
	from model.message import Message



	class AbsFlight(ABC):

		@abstractmethod
		def receiveMessage(self, message : Message ) -> None :
			pass

		@abstractmethod
		def getFlightCode( self ) -> str :
			pass

if __name__ == "__main__":
	print("""
		Boombastic
                 - Shaggy

[Intro]
Mr. Boombastic
What you want is a boombastic, romantic, fantastic lova'
Shaggy
Mr. Lover Lover, ummm
I'm Mr. Lover Lover, haha girl
Mr. Lover Lover
Mmmm, I'm Mr. Lover Lover

[Chorus]
She call me Mr. Boombastic
Tell me fantastic
Touch me on my back
She says I'm Mr. Ro.. Ro.. Mantic
Call me fantastic
Touch me on my back
She says I'm Mr. Ro...

[Verse 1]
Smooth
Just like a silk-a
Soft and cuddly, hug me up like a quilt
I'm a lyrical lover
No take me for no filth
With my sexual physique
Jah know me well-built
Oh me, oh my
Well, well, can't you tell
I'm just like a turtle
Crawling out of my shell?
Gal you captivate my body
Put me under a spell
With your Khus Khus perfume
I love your sweet smell
You're the only young girl
Who can ring my bell
And I can take rejection
So you tell me "Go to Hell"
		""")