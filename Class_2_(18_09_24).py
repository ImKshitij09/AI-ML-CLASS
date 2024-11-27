{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMWE94y15tBEXXpZ9ZdWFvd",
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
        "<a href=\"https://colab.research.google.com/github/ImKshitij09/AI-ML-CLASS/blob/main/Class_2_(18_09_24).py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "69lq2k6UH7WY"
      },
      "outputs": [],
      "source": [
        "import pandas as pd\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.metrics import mean_squared_error, r2_score\n",
        "\n",
        "# Load dataset\n",
        "energy_data = pd.read_csv('energy_dataset.csv')\n",
        "\n",
        "# Convert 'time' column to datetime and remove timezone information\n",
        "energy_data['time'] = pd.to_datetime(energy_data['time'], utc=True).dt.tz_localize(None)\n",
        "\n",
        "# Add temporal features\n",
        "energy_data['hour'] = energy_data['time'].dt.hour\n",
        "energy_data['day_of_week'] = energy_data['time'].dt.dayofweek\n",
        "energy_data['month'] = energy_data['time'].dt.month\n",
        "energy_data['year'] = energy_data['time'].dt.year\n",
        "\n",
        "# Group renewable and fossil energy generation\n",
        "renewable_sources = [\n",
        "    'generation biomass',\n",
        "    'generation hydro run-of-river and poundage',\n",
        "    'generation hydro water reservoir',\n",
        "    'generation marine',\n",
        "    'generation solar',\n",
        "    'generation wind offshore',\n",
        "    'generation wind onshore',\n",
        "    'generation other renewable'\n",
        "]\n",
        "\n",
        "fossil_sources = [\n",
        "    'generation fossil brown coal/lignite',\n",
        "    'generation fossil coal-derived gas',\n",
        "    'generation fossil gas',\n",
        "    'generation fossil hard coal',\n",
        "    'generation fossil oil',\n",
        "    'generation fossil oil shale',\n",
        "    'generation fossil peat'\n",
        "]\n",
        "\n",
        "energy_data['renewable_generation'] = energy_data[renewable_sources].sum(axis=1)\n",
        "energy_data['fossil_generation'] = energy_data[fossil_sources].sum(axis=1)\n",
        "\n",
        "# Prepare data for modeling\n",
        "model_data = energy_data[\n",
        "    [\n",
        "        'total load actual',\n",
        "        'total load forecast',\n",
        "        'renewable_generation',\n",
        "        'fossil_generation',\n",
        "        'hour',\n",
        "        'day_of_week',\n",
        "        'month',\n",
        "        'price day ahead',\n",
        "        'price actual'\n",
        "    ]\n",
        "].dropna()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Define features (X) and target (y)\n",
        "X = model_data.drop(columns=['total load actual'])\n",
        "y = model_data['total load actual']\n",
        "\n",
        "# Split data into training and testing sets\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "\n",
        "# Train a Linear Regression model\n",
        "model = LinearRegression()\n",
        "model.fit(X_train, y_train)\n",
        "\n",
        "# Predict on test set\n",
        "y_pred = model.predict(X_test)\n",
        "\n",
        "# Evaluate the model\n",
        "mse = mean_squared_error(y_test, y_pred)\n",
        "r2 = r2_score(y_test, y_pred)\n",
        "\n",
        "print(f\"Mean Squared Error: {mse}\")\n",
        "print(f\"R² Score: {r2}\")\n"
      ],
      "metadata": {
        "id": "t_5PvCX8XtOs",
        "outputId": "59fdd887-64a7-4248-9b2e-28bfa70d080c",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mean Squared Error: 186885.20117557625\n",
            "R² Score: 0.9909861000236088\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit\n",
        "import streamlit as st\n",
        "# Load the trained model\n",
        "model = LinearRegression()\n",
        "\n",
        "# Training code (use pre-trained weights in a real deployment)\n",
        "model.fit(X_train, y_train)\n",
        "\n",
        "st.title('Energy Demand Forecasting App')\n",
        "\n",
        "# File upload section\n",
        "uploaded_file = st.file_uploader(\"Upload your dataset (CSV)\", type=[\"csv\"])\n",
        "\n",
        "if uploaded_file:\n",
        "    # Read the uploaded file\n",
        "    new_data = pd.read_csv(uploaded_file)\n",
        "\n",
        "    # Feature engineering on new data\n",
        "    new_data['time'] = pd.to_datetime(new_data['time'], utc=True).dt.tz_localize(None)\n",
        "    new_data['hour'] = new_data['time'].dt.hour\n",
        "    new_data['day_of_week'] = new_data['time'].dt.dayofweek\n",
        "    new_data['month'] = new_data['time'].dt.month\n",
        "    new_data['renewable_generation'] = new_data[{renewable_sources}].sum(axis=1)\n",
        "    new_data['fossil_generation'] = new_data[{fossil_sources}].sum(axis=1)\n",
        "\n",
        "    # Select relevant features for prediction\n",
        "    features = new_data[['total load forecast', 'renewable_generation', 'fossil_generation',\n",
        "                         'hour', 'day_of_week', 'month', 'price day ahead', 'price actual']]\n",
        "\n",
        "    # Make predictions\n",
        "    predictions = model.predict(features)\n",
        "\n",
        "    # Display predictions\n",
        "    new_data['Predicted Load'] = predictions\n",
        "    st.write(new_data[['time', 'Predicted Load']])\n",
        "\n",
        "    # Download predictions\n",
        "    csv = new_data.to_csv(index=False).encode('utf-8')\n",
        "    st.download_button(\"Download Predictions\", data=csv, file_name=\"predictions.csv\")"
      ],
      "metadata": {
        "id": "oD3iwcMpAnpo",
        "outputId": "62212b55-dcfe-4531-ff18-e42e7bfab20a",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.40.2-py2.py3-none-any.whl.metadata (8.4 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.7)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (11.0.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.25.5)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.3.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (3.1.4)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<6,>=4.0->streamlit) (0.12.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.11)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=1.4.0->streamlit) (2024.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.4.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests<3,>=2.27->streamlit) (2024.8.30)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.1)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (24.2.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.35.1)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.21.0)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.16.0)\n",
            "Downloading streamlit-1.40.2-py2.py3-none-any.whl (8.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.6/8.6 MB\u001b[0m \u001b[31m53.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m82.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.40.2 watchdog-6.0.0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-11-27 11:46:16.846 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:46:17.039 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2024-11-27 11:46:17.045 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:46:17.048 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:46:17.051 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:46:17.054 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:46:17.058 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:46:17.060 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}