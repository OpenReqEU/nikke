# nikke
UH Cross Reference Detector for Qt Jira data.

This service was created as a result of the OpenReq project funded by the European Union Horizon 2020 Research and Innovation programme under grant agreement No 732463.

# Technical Description

Nikke checks cross references from Qt jira data comments and reports them as proposed dependencies.

## The following technologies are used:
- Python
- Docker
	
## Public APIs

POST http://217.172.12.199:9209/

## How to Install

With Docker installed:

docker build . -t nikke

docker run -p 9209:9209 nikke

## How to Use This Microservice

POST /

Include requirements in the request body. Returns a list of proposed dependencies.

## Notes for Developers

None at the moment.

## Sources

None

# How to Contribute
See the OpenReq Contribution Guidelines [here](https://github.com/OpenReqEU/OpenReq/blob/master/CONTRIBUTING.md).

# License

Free use of this software is granted under the terms of the [EPL version 2 (EPL2.0)](https://www.eclipse.org/legal/epl-2.0/).

