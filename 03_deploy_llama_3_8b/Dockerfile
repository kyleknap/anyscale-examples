# Nightly is needed until new release of Ray (as of March 25, 2026). Currently only the main
# branch supports the latest version of vLLM (0.18.0) which has support for loading model weights
# from Azure Blob Storage using Run:ai. This can be repinned to a specific version of Ray
# once a new release is available.
FROM anyscale/ray:nightly-py312-cu128
# Installs Ray Serve, RayLLM, and Run:ai Model Steamer dependencies
# that normally are not included in the base image.
RUN pip install ray[serve,llm] runai-model-streamer[azure]
