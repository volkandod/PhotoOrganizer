# PhotoOrganizer

  * A command-line tool to modify your photos' name to the date taken (yyyy-mm-dd hh-mm-ss.jpg).This tool uses exif data of the photo.
  * Your photos can be shown in chronological order.

## Installation

	# Clone the repo
	git clone https://github.com/volkandod/PhotoOrganizer.git
	cd PhotoOrganizer
	
	#Install dependencies
	sudo pip install -r requirements.txt

## Usage
	./PhotoOrganizer.py <directory>

## Example
	ls -l /tmp/Photo
		IMG_0711-original.JPG 
		IMG_0714-original.JPG  
		IMG_0818-original.JPG
	
	./PhotoOrganizer.py /tmp/Photo
		./IMG_0714-original.JPG  >> ./2017-08-31 18-06-52.jpg
		./IMG_0818-original.JPG  >> ./2017-09-16 17-09-11.jpg
		./IMG_0711-original.JPG  >> ./2017-08-31 18-05-36.jpg

	ls -l /tmp/Photo
                2017-08-31 18-05-36.jpg  
		2017-08-31 18-06-52.jpg 
		2017-09-16 17-09-11.jpg

