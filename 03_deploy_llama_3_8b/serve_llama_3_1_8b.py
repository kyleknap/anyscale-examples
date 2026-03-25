from ray import serve
from ray.serve.llm import LLMConfig, build_openai_app

llm_config = LLMConfig(
    model_loading_config=dict(
        model_id="my-llama-3.1-8B",
        # Specify the path to your model weights in your Azure Storage account. This should
        # include the container name and any blob prefix (e.g. folder path) to the weights.
        model_source="az://<container-name>/<path-to-llama3.1-8b-weights>",
    ),
    accelerator_type="A100",
    deployment_config=dict(
        autoscaling_config=dict(
            min_replicas=1, max_replicas=2,
        )
    ),
    runtime_env=dict(
        env_vars={
            # Specify the Azure Storage account name to use for loading model weights with
            # Run:ai model streamer. The environment's managed identity should have at least
            # "Blob Storage Data Reader" permissions to read from the storage account.
            "AZURE_STORAGE_ACCOUNT_NAME": "<storage-account-name>",
        }
    ),
    engine_kwargs=dict(
        max_model_len=8192,
        # Enables use of Run:ai model streamer for loading model weights.
        load_format="runai_streamer",
    ),
)

app = build_openai_app({"llm_configs": [llm_config]})

# Uncomment the below line to run the service locally with Python.
# serve.run(app, blocking=True)
