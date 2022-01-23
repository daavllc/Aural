# Aural
 Virtual audio cable creator, manager, and router

## Purpose:
When faced with a complex audio situtation, such as for streaming or recording, there is no non-proprietary solution to create virtual audio cables (VACs) or route audio sources to different destinations easily. To solve this issue, we will create an open-source alternative to proprietary virtual audio cable software, and proprietary audio routing software. We hope to create a single product that performs the tasks of both of the below examples, without the limitations of the free versions. 
 - Example VAC software: [Virtual Audio Cable (VAC)](https://vac.muzychenko.net/en/)
 - Example Routing software: [Voicemeeter Banana](https://vb-audio.com/Voicemeeter/banana.htm)

## Details:
 - Project Lead: [Anonoei](https://github.com/Anonoei)
 - Language: Python 3.10
 - License: [MIT](https://mit-license.org/)
 - Dependancies: dearpygui
 - Documentation: None (yet)

## Current status/roadmap:
 - [ ] Initial release
 - [ ] Documentation
   - [ ] Initial documentation
 - [ ] UI
   - [ ] CUI
     - [ ] Initial implementation
   - [ ] GUI
     - [ ] Initial implementation
 - [ ] Platform support
   - [X] Windows
   - [ ] Linux
   - [ ] MacOS
 - [ ] Routes
   - [ ] Features (in no particular order)
     - [ ] Equalizer
     - [ ] Echo
     - [ ] Reverb
     - [ ] Brightness
     - [ ] Compression
     - [ ] Noise Gate
     - [ ] Panning
     - [ ] Volume Control
   - [ ] Initial implementation
   - [ ] Input/Output
   - [ ] Find audio devices
 - [ ] Audio Cables
   - [ ] Initial implementation
   - [ ] Create audio cables

## Using Aural
 1. Download Aural
    - There are currently no releases, please follow the step 1 from `Contributing to Aural` below.
 2. Launch Aural
    - Use the provided launch script
    - Use python to launch [main.py](https://github.com/daavofficial/Aural/blob/main/src/main.py)
 3. Create a Virtual Audio Cable
    1. Click the Audio Cables tab
    2. Click Create
    3. (To be added at a later date)
 4. Create a Route
    1. Click the Routes tab
    2. Click Create
    3. (To be added at a later date)

## Contributing to Aural
 1. Download from source
    - Using Git: Run `git clone --recursive https://github.com/daavofficial/Aural.git`
    - Downloading: Click the `Code` button near the top right > Download ZIP, extract the file
      - To ensure all submodules are installed, run `git submodule init --recursive` inside the Aural folder after download
 2. Open the new `Aural` folder
 3. Have fun! (More to be added at a later date)

## License
Copyright © 2022 DAAV, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.