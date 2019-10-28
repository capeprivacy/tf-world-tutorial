# Federated Learning on Google Cloud Platform

This guide will show you how to launch Google Cloud instances to run the federated learning tutorial in the cloud.

If you want to run this part of the tutorial, you will need a [GCP account](https://cloud.google.com/) and to install [Google SDK](https://cloud.google.com/sdk/install). See [here](../README.md#google-cloud-installation) for a quick reference.

These commands should be run from `tools/gcp`:

```shell
cd <repo root>/tools/gcp
```

## Running

First, we need to specify all of the instance names we need. For private prediction we need seven servers three for the secure aggregation, one for the model owner and three for the data owners. We export an environement variable called `INSTANCE_NAMES` containing a list of the names.

```shell
export INSTANCE_NAMES="server0 server1 server2 model-owner data-owner-0 data-owner-1 data-owner-2"
```

If using zshell instead of bash, you can switch the above assignment to:

```shell
export INSTANCE_NAMES=( server0 server1 crypto-producer model-owner data-owner-0 data-owner-1 data-owner-2 )
```

### Setup instances

Next we can launch the instances with a helper script:

```shell
TFE_IMAGE=docker.io/tfencrypted/tf-encrypted:0.6.0-rc0 ./create $INSTANCE_NAMES
```

Alternatively, if they have already been created but are currently terminated, simply start them again with

```shell
./start $INSTANCE_NAMES
```

This causes the instances to launch a docker container that runs the TF Encrypted servers. At this point they are waiting for the configuration file that will be used to connect to other servers.

### Linking Instances

We can generate and share a configuration file amongst all of the instance with:

```shell
./link $INSTANCE_NAMES
```

This uses the instances external addresses to connect one another and also opens a port on each instance at 4440.

### Running the Notebooks

At this point you can go to back to the notebook `c - Running Federated Computations in the cloud.ipynb` and run all the cells there to see the federated learning happen.

### Cleaning Up

Once done, the instances can either simply be stopped with:

```shell
./stop $INSTANCE_NAMES
```

or destroyed entirely with

```shell
./delete $INSTANCE_NAMES
```