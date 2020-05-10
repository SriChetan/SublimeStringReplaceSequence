# Sublime StringReplaceSequence
A sublime plugin to create custom commands of replace sequence


## Installation


### Manual Installation

**Sublime Text 4**

- `cd <Packages directory>` (MacOS: `~/Library/Application\ Support/Sublime\ Text/Packages`)
- `git clone https://github.com/dzhibas/SublimePrettyJson.git "Pretty JSON"`


## Usage

Open Sublime windown and write the replace sequences in below JSON format

Ex: First insert Hello at the begining of every line then insert World to the end of every line
{
  "commands": [
    {
      "Find": "^",
      "Replace": "Hello"
    },
    {
      "Find": "$",
      "Replace": "World"
    }
  ],
  "name": "ExampleReplace"
}

Enter <kbd>cmd+ctrl+j</kbd> and select Create Replace Sequence

The command is created with command as example_sequence


Now open a sublime window where you need to use the relace sequence. 
Enter <kbd>cmd+ctrl+j</kbd> , search for example sequence and click enter. 
The relace operations are performed on the active window
