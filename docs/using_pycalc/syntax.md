# Using PyCalc
## Syntax
In PyCalc, commands have their arguments split by spaces

### calc
Solves the provided equation
`calc [int] [op] [int]`

Operations include;
- Addition: + or `-add`
- Subtraction: - or `-sub`
- Multiplication: * or x or `-mlt`
- Division: / or `-div`

### get
`get [-eq|-user] [id]`

- `-eq`: Provides details on an equation from the EID
- `-user`: Provides details on a user from the UID

### me
- No Arguments: Displays username and UID of logged in account
- `-history`: Displays the equation ids of every equation calculated with the logged in account

### docs
- No Arguments: Shows link to this documentation
- `-credits`: Shows who made this project possible
- `-repo`: Show link to the GitHub repository