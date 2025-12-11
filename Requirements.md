# RedEye Rquirements

## Abstract
`This Document shows the Technical Non Technical Requirements for our online activites social analysis along with Testing Criteria and a brief introduction to the archeticture of the solution which can be viewd in the technical specifications`

## Technical Requirements
- Ingesting users
- Ingesting social comments and written interactions
- Ingesting online groups and societis including pages and groups
- Ingesting online social events
- Ingesting online social person related entities
- Create all possible Relationships between entities
- Train a pipeline of ML Models on the domain specific data
- Give a report about a user called "User's Social Profile" contains it's Big 5 OCEAN Traits analysis and it's behavioral analysis 


## Non Technical Rrequirements
- Security: Protect users data and keep it's privacy.
- Availability: Enough availability to handle each request incoming to the system.
- Scalability: since this solution can operate as a service it's necessery for it to be scalable and extendable.
- Flexability: since this solution can operate as a service it's necessery for it to have the ability to work as a singular independant unit that can be replaced, updated, and deployed directly.

## Testing Criteria

### Entry Testing Criteria
- Required Connections established
- Required Data exist
- Configurations required for the functions established
- Setting Environment variables and setting a default on fail values

### Exit Testing Criteria
- No critical bugs

### Acceptance Criteria

### Perforemence Testing Criteria
