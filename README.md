# File Structure
src/
│── presets/                             # Configuration preset
│   │── react-ts-fastapi-lambda.json
│── templates/                           # Template components
│   │── frontend/                        
│   │   ├── react/js/
│   │   ├── react/ts-testing-library/    
│   │── backend/                         
│   │   ├── python/fastapi/     
│   │── infrastructure/                 
│   │   ├── terraform/aws-lambda-vpc/    
│   │   ├── terraform/aws-monolith/
│   │── docker/                          
│   │   ├── react/
│   │   ├── python-fastapi/
│   │   ├── postgres/
│   │   ├── redis/
│   │── ci-cd/                          
│   │   ├── github-actions/
│   │   │   ├── react.yml
│   │   │   ├── fastapi.yml
│── generators/                          
│   │── generate_component.py            
│   │── frontend_generator.py            
│   │── backend_generator.py             
│   │── infrastructure_generator.py      
│   │── docker_generator.py              
│   │── ci_cd_generator.py               
│   │── git_generator.py                 
│   │── project_generator.py             
│── outputs/                             
│── cli.py                               
│── main.py                              
│── README.md                           
│── requirements.txt