# ReactJs development environment

## Software prerequisites

* Docker
* Node
* Yarn
* VSCode or WebStorm
* Git

To start working on Tracardi GUI clone tracardi-gui repo.

```bash
git clone http://github.com/tracardi/tracardi-gui  #(1)
```

1. Clones GUI source code from GitHub

Then run:

```bash
yarn install  #(1)
```

1. This will install all project dependencies.

## Starting GUI

In the project directory, run:

```bash
yarn start
```

This will run the app in the development mode. Open [http://localhost:3000](http://localhost:3000) to view it in the
browser. The page will reload if you edit source code. You will also see any lint errors in the console.

!!! Info 

    In order to work with GUI you will need Tracardi API. Below you will find instructions how to run API with docker.

## Dependencies

Tracardi GUI depends on 1 service Tracardi-API ([API Installation](../../installation/opensource/docker/docker.md#start-tracardi-api)), but API depends on other
services that [must be installed](../../installation/dependencies/index.md) as well.




