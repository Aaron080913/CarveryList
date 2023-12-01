# Carvery Ordering Station

Carvery Ordering Station is a python terminal Data analyser, which runs in the code institute mock terminal on Heroku. 

Users have to enter their Sunday Carvery orders into the terminal so that the kitchen is able to make the orders and so that they can keep a running average of how many different roasts they will need for the next coming week. and this is seen in a seperate worksheet file.

![Responsice Mockup](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Am_I_Responsive_Carvery.jpeg)

## How to use

The user has to input what type of roast that they would like to order by filling out 7 numbers to indicate which type of roast they would like to order. if the user does not put 7 numbers with commas into the input data then an error message will be displayed and the user will be asked to enter correct numbers.

## Features 

### Existing Features

- __Initial User Information__

  - This Gives the User the Information that is needed to be able to correctly enter values so that the ordering system can work.

![User Info](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Initial%20User%20information..jpeg)

- __The Data Input Section__

  - This is where the User inputs their order for which Roasts they want.

![User Input](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Data%20Input%20Section.jpeg)

- __The Data Input Results__

  - If the User enters Data that does not conform to the initial Data input rules then A error message will be displayed and ask for the USer to re-enter the details. 

  ![Incorrect Data](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Incorrect%20Data%20Input%20Message.jpeg)

  - If the User enters Data that does conform to the Guidelines then it will state that the data is valid. 

![Data is Valid](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Data%20is%20Valid!.jpeg)

- __Worksheets Updates/Calculations__

  - This is where you will see the data being updated, and will let you know that it has been updated successfully. 

![Sales](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Sales%20Worksheet.jpeg)

![Stock](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Stock%20Worksheet.jpeg)

![Surplus](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Surplus%20Worksheet.jpeg)

- __The Worksheet__ 

  - The Worksheet is where the Data input is sent to be calculated to work out Surplus, and to get an average sales estimate for the next Weekend Sales.

![Worksheet Before](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Carvery%20Worksheet%20sales%20Before.jpeg)

![Worksheet After](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/Sales%20After.jpeg)

## Testing 

I have tested this project by doing the following:

- Passed the code through a PEP8 Python Validator, to find only one issue being a blank line at the end of the file which is A known issue with the validator.

![pep_8](https://github.com/Aaron080913/CarveryList/blob/main/assets/images/PEP8.jpeg)

- invalid inputs - not allowed to input less/more then 7 intergers, or to have strings where intergers ar expected.
- Tested in local terminal and the code institute Herokus terminal.

## Deployment

This project was deployed using Code Institutes mock terminal for Heroku.

- Steps for Deployment:
    - fork or clone this Repository
    - Create A new Heroku account app
    - set the buildbacks to python and Nodejs in that order
    - Link the Heroku app to the Repository
    - click on Deploy

## Credits 

- Code Institute for the deployment terminal.  
