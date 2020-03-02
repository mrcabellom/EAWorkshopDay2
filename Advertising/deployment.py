from azureml.core import Workspace
from azureml.core.model import Model
from azureml.core.webservice import AciWebservice,Webservice
from azureml.core.image import ContainerImage


if __name__ == "__main__":

    try:
        ws = Workspace.from_config(path="config/azureml_ws.json")
        print('Library configuration succeeded')
    except:
        print('Workspace not found')


    aciconfig = AciWebservice.deploy_configuration(cpu_cores=2, 
                                                memory_gb=2, 
                                                tags={"data": "marketing",  
                                                        "method": "sklearn"},
                                                description='Sales Regression')


    image_config = ContainerImage.image_configuration(execution_script="score.py",
                                                        runtime="python",
                                                        conda_file="../environment.yml",
                                                        description="image for model"
                                                        )

    model = Model(workspace=ws,name='RandomForestregressor')

    image = ContainerImage.create(workspace=ws, 
                        name='rfservice',
                        models=[model],
                        image_config=image_config)

    image.wait_for_creation(show_output=True)

    service = Webservice.deploy_from_image(ws,'rfservice',image,deployment_config=aciconfig)
    
    # service = Webservice(workspace=ws,name="rfservice")
    # print(service.state)
    # service.update(image=image)
    # service.wait_for_deployment(show_output=True)


