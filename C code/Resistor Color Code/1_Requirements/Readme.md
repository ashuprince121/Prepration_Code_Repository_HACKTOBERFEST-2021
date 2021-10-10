# Requirements
# Introduction
- Education is very vast, their countless formulas and especially in Engineering branch which is itself subdivided into many subjects/fields. Hence, it becomes very difficult to remember them all.
- A **resistor** is one of the basic Electrical devices used in our day-to-day life and almost every Electronic circuit so it becomes necessary to  calculate the resistance of a physical resistor on regular basis for an Engineer.
- This project aims to **reduce** the **burden or effort** and **save the time** which was to be put to calculate and remember the formula to find the resistance value of a **five-band** physical resistor.

# Research

## 1. How does the resistor color code work?
Resistor esteems are frequently demonstrated with shading codes. Essentially all leaded resistors with a rating of up to one watt are set apart with shading groups. The coding is characterized in the global standard IEC 60062. This standard depicts the stamping codes for resistors and capacitors. It incorporates likewise mathematical codes, concerning models frequently utilized for SMD resistors. The shading code is given by a few groups. Together they indicate the obstruction esteem, the resistance, and in some cases the unwavering quality or disappointment rate. The quantity of groups differs from three to six. As a base, two groups show the opposition worth and one band fills in as a multiplier. The obstruction esteems are normalized, these qualities are called favored worth.

## 2. Resistor Color Code Chart
The chart below shows the resistance and tolerance for resistors. The table can also be used to determine color of the bands when the values are known.

<div align="center">
<img src="https://eepower.com/uploads/education/resistor_color_codes_chart.png" >
</div>

## 3. Tips for Reading Resistor Codes
- The reading direction may not generally be clear. Here and there the expanded space between band 3 and 4 provides away the understanding guidance. Additionally, the primary band is normally the nearest to a lead. A gold or silver band (the resistance) is consistently the last band. 
- It is a decent practice to check the producer's documentation to make certain about the pre-owned coding framework. Surprisingly better is to gauge the obstruction with a multi-meter. At times this may even be the best way to sort out the opposition; for instance when the shading groups are singed off.
## 4. Five Band Resistor
Resistors with high quality have an additional band to show a third critical digit. In this way, the initial three groups demonstrate the critical digits, the fourth band is the increase factor and the fifth band addresses the resistance. There are special cases for this. For instance, here and there the additional band shows disappointment rate (military detail) or temperature coefficient (more seasoned or concentrated resistors). If it's not too much trouble, read the segment "Color code exception for more data.
## 5. Color Code Exception (NOT INCLUDED IN PROJECT)
Five band resistor with a 4th band of gold or silver :
- Resistors with high quality have an additional band to show a third critical digit. In this way, the initial three groups demonstrate the critical digits, the fourth band is the increase factor and the fifth band addresses the resistance. There are special cases for this. For instance, here and there the additional band shows disappointment rate (military detail) or temperature coefficient (more seasoned or concentrated resistors). If it's not too much trouble, read the segment "Shading code special cases for more data.
## 6. Purpose and Benefits
### Physical :
There are many clear benefits to utilizing a shading coding framework on electrical and electronic segments. The benefit of utilizing shaded rings or groups around a resistor's body is that they can be effortlessly seen and perused regardless of the position or direction of the resistor on board. These shaded groups can likewise be perused regardless of whether the body of the resistor is somewhat grimy or seriously consumed.
### Program :
The implementation is done while aiming to reduce the effort and time required to calculate the resistance and provide a seamless experience.

# Cost and Features
<div align="center">
<img src="https://github.com/VisheshYadav288037/Advanced-Electrical-Electronics/blob/master/1_Requirements/table.png" >
</div>


# Defining Our System
## Assumptions :
1. User have read the **resistance color table** mentioned in Research part.
2. User understands and is able to enter color band as asked in program.
3. The program is limited to **five band resistors only**.
4. The exception in five band register discussed in Color Code Exception part of Research is not supported by program.
## Flow Chart :
<div align="center">
<img src="https://github.com/VisheshYadav288037/Advanced-Electrical-Electronics/blob/master/1_Requirements/Flow%20chart%201.png" >
</div>
1. INPUT: Take input of 5 color bands from user<br>
2. FindColor: Function which will further call UpperToLower and CompareColor function and will return address of found colors<br>
3. UpperToLower: Function which will convert all uppercase char in a string to lowercase<br>
4. CompareColor: Function which will check if the inpput is invalid or not<br>
5. If error is found Jump to step number '8' else pass value to UnitFinder<br>
6. Get tolerance for respective input<br>
7. Combine tolerance and resistance together and print them<br>
8. Ask the user if he want to start over again<br>
9. If user enters 'Y' then go to step '1' else end the program<br>
                                                                                                                           
# SWOT ANALYSIS :                                                                                                                         
<div align="center">
<img src="https://github.com/VisheshYadav288037/Advanced-Electrical-Electronics/blob/master/1_Requirements/SWOT%20L.png" >
</div>

# 4W&#39;s and 1&#39;H

## Who:

- **Engineers**
- **Technicians**
- **Element and Circuit Manufacturers**

## What:

- **Human error**
- **Lot of time consumption**
- **Tiredness after multiple calculation**

## When:

- **While Manufacturing**
- **While Diagnosing**
- **During research** 

## Where:

- **In Industries**
- **In Circuits**
- **In labs**


## How:

- **Manually  calculating the resistance of many resistor by band method continously leads to error, tierdness and waste of time**


# Detail requirements
## High Level Requirements:
| ID | Description |  Status | 
| ----- | ----- | ---------|
| HL1 | User should get welcome message |  IMPLEMENTED  |
| HL2 | User should be able to insert color for give bands | IMPLEMENTED | 
| HL3 | User shall be able to get resistance value |  IMPLEMENTED  |
| HL4 | User shall be able to get tolerance value |  IMPLEMENTED  |
| HL5 | User should get successfull message |IMPLEMENTED |
| HL6 | User should be asked to start over again or exit  |  IMPLEMENTED  |
| HL7 | User should not get output if wrong color inserted |  IMPLEMENTED  |
| HL8 | User should get error message | IMPLEMENTED |
| HL9 | Prompt to view resistance color band table | FUTURE |
| HL10 | User will be asked to input the number of bands for resistor | FUTURE |


##  Low level Requirements:
| ID | Description | Status  |
| ------ | --------- |  ----- |
| LL1 | User will get a **WELCOME** message on the top of home window letting them know that this is the starting page | IMPLEMENTED  |
| LL2 | (1). User should follow proper format of inserting the color bands as asked                                                                                                 (2). User should be able to see his input. | IMPLEMENTED  |
| LL3 | Resistance value should be displayed in **Ohms** and sepated by digit place. | IMPLEMENTED |
| LL4 | Tolerance value should be displayed in **%**. | IMPLEMENTED |
| LL5 | A **HURRAY** message will appear to top of succesfull page letting user know that computation was succesfull. |  IMPLEMENTED  |
| LL6 | If the output is successfull or invalid the user should be asked to either start again by inserting color bands or exit the program |  IMPLEMENTED  |
| LL7 | If an invalid input is given by user then he must be informed about that particular invalid input and no resistance and tolerance value should be provided. |  IMPLEMENTED  |
| LL8 | User will get **AW SNAP** message to let them know that they have entered a wrong input | IMPLEMENTED  |
| LL9 | User will be provided option to view the resistance band table to crosscheck the output |  FUTURE  |
| LL10 | User will be able to get output for different band resistors |  FUTURE  |
