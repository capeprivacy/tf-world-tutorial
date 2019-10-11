# Private Predictions On Google Cloud Platform

This guide will show you how to launch Google Cloud instances to run private predictions in the cloud.

All steps here assume that you have a Google Cloud account, [Cloud SDK](https://cloud.google.com/sdk/) has already been installed (for macOS this may be done via e.g. Homebrew: `brew cask install google-cloud-sdk`) and a project set up.

If not already done you'll need to clone the git repository `https://github.com/tf-encrypted/tf-encrypted`. These commands will be run from within the repo (`cd tf-encrypted/tools/gcp`).

## Running

First, we need to specify all of the instance names we need. For private prediction we only need three `server0`, `server1` and `server2`. We export an environement variable called `INSTANCE_NAMES` containing a list of the names.

```shell
export INSTANCE_NAMES="server0 server1 server2"
```

### Setup instances

Next we can launch the instances with a helper script:

```shell
./create $INSTANCE_NAMES
```

Alternatively, if they have already been created but are currently terminated, simply start them again with

```shell
./start $INSTANCE_NAMES
```

This causes the instance to launch a docker container that runs the TF Encrypted server. At this point they are waiting for a configuration to use to connect to other servers.

### Linking Instances

We can generate and share a configuration file amongst all of the instance with:

```shell
./link $INSTANCE_NAMES
```

This uses the instances external addresses to connect one another and also opens a port on each instance at 4440.

### Running the Notebooks

At this point you can go to back to the notebook `d - Secure Model Serving Cloud Edition.ipynb` and run the cells there and then back to `c - Private Prediction Client.ipynb` to run the actual prediction.

### Cleaning Up

Once done, the instances can either simply be stopped with:

```shell
./stop $INSTANCE_NAMES
```

or destroyed entirely with

```shell
./delete $INSTANCE_NAMES
```
