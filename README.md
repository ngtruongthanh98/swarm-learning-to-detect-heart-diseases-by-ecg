# Swarm Learning for Heart Disease Detection

This project is focused on using swarm learning and big data to build a model that can detect heart disease. The dataset used in this project is collected from Kaggle and is available at the following links:

- https://www.kaggle.com/datasets/vlbthambawita/deepfake-ecg
- https://www.kaggle.com/code/bjoernjostein/deepfake-ecg-generator

Swarm learning is a novel approach to machine learning that utilizes decentralized computing to enable data sharing and collaborative learning while maintaining privacy and data security. This approach is particularly well-suited for large-scale datasets where traditional machine learning methods may not be feasible.

The project's tech stack includes:

- Model ANN (Python)
- Backend: Golang
- Frontend: NuxtJS (VueJS)
- Cloud service: GCP (or AWS)

By leveraging the power of swarm learning and big data, we aim to create a model that can accurately detect heart disease and improve patient outcomes.

Frontend - NuxtJS

![Analyze ECG page](https://iili.io/HhBmRmg.png "Analyze page").

![Hospital page](https://iili.io/HhBmM7t.png "Hospital page").


# How to run the project?
## Frontend
- Install docker, follow the instruction in the directory /ecg-portal/docker-instruction.md
- Or running local, required: node v16.15.0 +
```
cd ecg-portal
```

```
yarn
```

```
yarn serve
```

- Access http://localhost:3000

## Backend
Required: Install all packages which use by models
- Install python3
- Install joblib version 1.2.0
- tensorflow==2.12.0
- numpy
- sklearn
- pandas

```
cd backend
```

```
python3 main.py
```

Backend will run on http://localhost:5000
