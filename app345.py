{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPyhL8qwI6rQLy6YmTp0Y77",
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
        "<a href=\"https://colab.research.google.com/github/ImKshitij09/AI-ML-CLASS/blob/main/app345.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "69lq2k6UH7WY",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "28b07730-954d-4958-f35a-8c84d69cd588"
      },
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
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m3.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
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
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.6/8.6 MB\u001b[0m \u001b[31m26.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m59.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.40.2 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit pyngrok"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "TtrCSs0ZOD_t",
        "outputId": "635930bb-2fe4-42e3-e4fe-7e7aa382d72a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.10/dist-packages (1.40.2)\n",
            "Collecting pyngrok\n",
            "  Downloading pyngrok-7.2.1-py3-none-any.whl.metadata (8.3 kB)\n",
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
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.1.43)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.9.1)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.3)\n",
            "Requirement already satisfied: PyYAML>=5.1 in /usr/local/lib/python3.10/dist-packages (from pyngrok) (6.0.2)\n",
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
            "Downloading pyngrok-7.2.1-py3-none-any.whl (22 kB)\n",
            "Installing collected packages: pyngrok\n",
            "Successfully installed pyngrok-7.2.1\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Load the trained model\n",
        "model_path = 'energy_forecasting_model.pkl'\n",
        "model = joblib.load(model_path)\n",
        "\n",
        "# Define the Streamlit app\n",
        "def app():\n",
        "    st.title(\"Energy Demand Forecasting App\")\n",
        "\n",
        "    st.header(\"Input Features\")\n",
        "    # Create input fields for features\n",
        "    total_load_forecast = st.number_input(\"Total Load Forecast (MW)\")\n",
        "    renewable_generation = st.number_input(\"Renewable Generation (MW)\")\n",
        "    fossil_generation = st.number_input(\"Fossil Generation (MW)\")\n",
        "    price_actual = st.number_input(\"Price Actual (€/MWh)\")\n",
        "    price_day_ahead = st.number_input(\"Price Day Ahead (€/MWh)\")\n",
        "    hour = st.number_input(\"Hour of Day (0-23)\", min_value=0, max_value=23, step=1)\n",
        "    day_of_week = st.number_input(\"Day of Week (0=Monday, 6=Sunday)\", min_value=0, max_value=6, step=1)\n",
        "    month = st.number_input(\"Month (1-12)\", min_value=1, max_value=12, step=1)\n",
        "\n",
        "    # Prepare input data\n",
        "    input_data = pd.DataFrame({\n",
        "        'total load forecast': [total_load_forecast],\n",
        "        'renewable_generation': [renewable_generation],\n",
        "        'fossil_generation': [fossil_generation],\n",
        "        'price actual': [price_actual],\n",
        "        'price day ahead': [price_day_ahead],\n",
        "        'hour': [hour],\n",
        "        'day_of_week': [day_of_week],\n",
        "        'month': [month]\n",
        "    })\n",
        "\n",
        "    # Predict button\n",
        "    if st.button(\"Predict\"):\n",
        "        prediction = model.predict(input_data)[0]\n",
        "        st.success(f\"Predicted Total Load: {prediction:,.2f} MW\")\n",
        "\n",
        "# Run the app\n",
        "if __name__ == \"__main__\":\n",
        "    app()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "O2o0f8tnHegk",
        "outputId": "62de6d5d-755b-48c1-d26c-935bd2c68215"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-11-27 15:37:36.510 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.514 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.515 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.519 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.521 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.523 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.525 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.528 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.529 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.536 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.537 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.540 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.541 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.542 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.543 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.544 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.545 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.547 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.550 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.552 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.553 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.554 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.555 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.556 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.558 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.559 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.560 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.561 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.562 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.563 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.564 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.566 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.567 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.568 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.569 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.570 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.571 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.572 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.573 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.574 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.575 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.576 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.577 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.579 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.580 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.581 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.582 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.583 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.584 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.585 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.586 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.592 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.593 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.594 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.596 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 15:37:36.597 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    }
  ]
}