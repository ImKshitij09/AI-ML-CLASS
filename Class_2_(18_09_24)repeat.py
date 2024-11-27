{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP5WxO1MvcESCHGy5kYTnXc",
      "include_colab_link": True
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
        "<a href=\"https://colab.research.google.com/github/ImKshitij09/AI-ML-CLASS/blob/main/Class_2_(18_09_24)repeat.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "69lq2k6UH7WY",
        "outputId": "461eca59-3116-4edd-ad92-e25e3a0cca0b",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
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
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m858.6 kB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
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
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.6/8.6 MB\u001b[0m \u001b[31m23.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m31.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m6.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.40.2 watchdog-6.0.0\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-11-27 11:57:16.679 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.830 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.10/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2024-11-27 11:57:16.832 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.835 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.838 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.841 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.842 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.845 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.846 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2024-11-27 11:57:16.849 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit\n",
        "import streamlit as st\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt\n",
        "import seaborn as sns\n",
        "from sklearn.linear_model import LinearRegression\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import mean_squared_error, r2_score\n",
        "\n",
        "# Title of the Streamlit app\n",
        "st.title(\"Interactive Energy Demand Forecasting App\")\n",
        "\n",
        "# Section 1: Upload Dataset\n",
        "st.header(\"Step 1: Upload Dataset\")\n",
        "uploaded_file = st.file_uploader(\"Upload your dataset (CSV)\", type=[\"csv\"])\n",
        "\n",
        "if uploaded_file:\n",
        "    # Load the dataset\n",
        "    energy_data = pd.read_csv(uploaded_file)\n",
        "\n",
        "    # Display a preview of the dataset\n",
        "    st.subheader(\"Dataset Preview\")\n",
        "    st.write(energy_data.head())\n",
        "\n",
        "    # Convert 'time' column to datetime and add temporal features\n",
        "    energy_data['time'] = pd.to_datetime(energy_data['time'], utc=True).dt.tz_localize(None)\n",
        "    energy_data['hour'] = energy_data['time'].dt.hour\n",
        "    energy_data['day_of_week'] = energy_data['time'].dt.dayofweek\n",
        "    energy_data['month'] = energy_data['time'].dt.month\n",
        "\n",
        "    # Aggregate renewable and fossil energy generation\n",
        "    renewable_sources = [\n",
        "        'generation biomass', 'generation hydro run-of-river and poundage',\n",
        "        'generation hydro water reservoir', 'generation marine', 'generation solar',\n",
        "        'generation wind offshore', 'generation wind onshore', 'generation other renewable'\n",
        "    ]\n",
        "    fossil_sources = [\n",
        "        'generation fossil brown coal/lignite', 'generation fossil coal-derived gas',\n",
        "        'generation fossil gas', 'generation fossil hard coal', 'generation fossil oil',\n",
        "        'generation fossil oil shale', 'generation fossil peat'\n",
        "    ]\n",
        "    energy_data['renewable_generation'] = energy_data[renewable_sources].sum(axis=1)\n",
        "    energy_data['fossil_generation'] = energy_data[fossil_sources].sum(axis=1)\n",
        "\n",
        "    # Section 2: Data Visualization\n",
        "    st.header(\"Step 2: Data Visualization\")\n",
        "\n",
        "    # Renewable vs Fossil Energy\n",
        "    st.subheader(\"Total Renewable vs Fossil Energy Generation\")\n",
        "    fig, ax = plt.subplots()\n",
        "    ax.bar(['Renewable', 'Fossil'], [\n",
        "        energy_data['renewable_generation'].sum(),\n",
        "        energy_data['fossil_generation'].sum()\n",
        "    ])\n",
        "    st.pyplot(fig)\n",
        "\n",
        "    # Time-series of energy generation\n",
        "    st.subheader(\"Energy Generation Over Time\")\n",
        "    fig, ax = plt.subplots(figsize=(12, 6))\n",
        "    ax.plot(energy_data['time'], energy_data['renewable_generation'], label='Renewable')\n",
        "    ax.plot(energy_data['time'], energy_data['fossil_generation'], label='Fossil')\n",
        "    ax.legend()\n",
        "    st.pyplot(fig)\n",
        "\n",
        "    # Section 3: Train and Predict\n",
        "    st.header(\"Step 3: Train and Predict\")\n",
        "\n",
        "    # Prepare data for training\n",
        "    model_data = energy_data[\n",
        "        ['total load actual', 'total load forecast', 'renewable_generation', 'fossil_generation',\n",
        "         'hour', 'day_of_week', 'month', 'price day ahead', 'price actual']\n",
        "    ].dropna()\n",
        "\n",
        "    X = model_data.drop(columns=['total load actual'])\n",
        "    y = model_data['total load actual']\n",
        "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
        "\n",
        "    # Train a Linear Regression model\n",
        "    model = LinearRegression()\n",
        "    model.fit(X_train, y_train)\n",
        "\n",
        "    # Predictions\n",
        "    y_pred = model.predict(X_test)\n",
        "    mse = mean_squared_error(y_test, y_pred)\n",
        "    r2 = r2_score(y_test, y_pred)\n",
        "\n",
        "    # Display metrics\n",
        "    st.subheader(\"Model Performance\")\n",
        "    st.write(f\"Mean Squared Error (MSE): {mse}\")\n",
        "    st.write(f\"R² Score: {r2}\")\n",
        "\n",
        "    # Allow the user to make predictions\n",
        "    st.subheader(\"Make Predictions on New Data\")\n",
        "    if st.checkbox(\"Use uploaded dataset for predictions?\"):\n",
        "        features = X_test\n",
        "        predictions = model.predict(features)\n",
        "\n",
        "        # Display predictions\n",
        "        predictions_df = pd.DataFrame({\n",
        "            \"Time\": energy_data['time'].iloc[features.index],\n",
        "            \"Predicted Load\": predictions\n",
        "        })\n",
        "        st.write(predictions_df)\n",
        "\n",
        "        # Download predictions\n",
        "        csv = predictions_df.to_csv(index=False).encode('utf-8')\n",
        "        st.download_button(\"Download Predictions as CSV\", data=csv, file_name=\"predictions.csv\")\n"
      ]
    }
  ]
}