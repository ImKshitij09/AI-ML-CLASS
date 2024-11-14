{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPB3s429hmc55oXFxCODkVE",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ImKshitij09/AI-ML-CLASS/blob/main/miami_housing_app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "MpKSF1jwXh_1"
      },
      "outputs": [],
      "source": [
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.linear_model import LinearRegression\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install -q streamlit"
      ],
      "metadata": {
        "id": "pMvtHsPIYGyd"
      },
      "execution_count": 8,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import joblib\n"
      ],
      "metadata": {
        "id": "2DL8UQDlX2-u"
      },
      "execution_count": 5,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "model = joblib.load('Kshitij_housing_pvt_ltd.joblib')\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 263
        },
        "id": "BfNplts3YyXi",
        "outputId": "e56b3198-e8eb-48d0-cfbc-a00c0c45aa22"
      },
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "error",
          "ename": "FileNotFoundError",
          "evalue": "[Errno 2] No such file or directory: 'Kshitij_housing_pvt_ltd.joblib'",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-6-bf290b703df5>\u001b[0m in \u001b[0;36m<cell line: 1>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mmodel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mjoblib\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mload\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'Kshitij_housing_pvt_ltd.joblib'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/joblib/numpy_pickle.py\u001b[0m in \u001b[0;36mload\u001b[0;34m(filename, mmap_mode)\u001b[0m\n\u001b[1;32m    648\u001b[0m             \u001b[0mobj\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_unpickle\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfobj\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    649\u001b[0m     \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 650\u001b[0;31m         \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfilename\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m'rb'\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    651\u001b[0m             \u001b[0;32mwith\u001b[0m \u001b[0m_read_fileobject\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mf\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mfilename\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmmap_mode\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mfobj\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    652\u001b[0m                 \u001b[0;32mif\u001b[0m \u001b[0misinstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mfobj\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mstr\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'Kshitij_housing_pvt_ltd.joblib'"
          ]
        }
      ]
    }
  ]
}