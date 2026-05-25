{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "b432b233",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-05-04 19:54:29.043 INFO    numexpr.utils: NumExpr defaulting to 8 threads.\n"
     ]
    },
    {
     "ename": "ModuleNotFoundError",
     "evalue": "No module named 'altair.vegalite.v4'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mModuleNotFoundError\u001b[0m                       Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\NILANJ~1\\AppData\\Local\\Temp/ipykernel_15488/3163941772.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[1;32m----> 1\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mst\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      2\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpickle\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mre\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mnltk\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\__init__.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     68\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0msource_util\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0m_source_util\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     69\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mstring_util\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0m_string_util\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 70\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdelta_generator\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mDeltaGenerator\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0m_DeltaGenerator\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     71\u001b[0m from streamlit.runtime.scriptrunner import (\n\u001b[0;32m     72\u001b[0m     \u001b[0madd_script_run_ctx\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0m_add_script_run_ctx\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\delta_generator.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     88\u001b[0m \u001b[1;31m# We select between them with the DataFrameElementSelectorMixin.\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     89\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0melements\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marrow\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mArrowMixin\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 90\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0melements\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marrow_altair\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mArrowAltairMixin\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     91\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0melements\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0marrow_vega_lite\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mArrowVegaLiteMixin\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     92\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mstreamlit\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0melements\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlegacy_data_frame\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mLegacyDataFrameMixin\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\anaconda3\\lib\\site-packages\\streamlit\\elements\\arrow_altair.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     33\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0maltair\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0malt\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     34\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mpandas\u001b[0m \u001b[1;32mas\u001b[0m \u001b[0mpd\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 35\u001b[1;33m \u001b[1;32mfrom\u001b[0m \u001b[0maltair\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mvegalite\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mv4\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapi\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mChart\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     36\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0mpandas\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mapi\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mtypes\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0minfer_dtype\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     37\u001b[0m \u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mModuleNotFoundError\u001b[0m: No module named 'altair.vegalite.v4'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import re\n",
    "import nltk\n",
    "\n",
    "from nltk.corpus import stopwords\n",
    "from nltk.stem import WordNetLemmatizer\n",
    "\n",
    "# Load saved objects\n",
    "model = pickle.load(open(\"model.pkl\", \"rb\"))\n",
    "vectorizer = pickle.load(open(\"vectorizer.pkl\", \"rb\"))\n",
    "encoder = pickle.load(open(\"encoder.pkl\", \"rb\"))\n",
    "\n",
    "# NLP setup\n",
    "nltk.download('stopwords')\n",
    "nltk.download('wordnet')\n",
    "\n",
    "stop_words = set(stopwords.words('english'))\n",
    "stop_words.discard('not')\n",
    "\n",
    "lemmatizer = WordNetLemmatizer()\n",
    "\n",
    "# Preprocessing function (same as training)\n",
    "def preprocess(text):\n",
    "    text = text.lower()\n",
    "    text = re.sub(r\"http\\S+\", \"\", text)\n",
    "    text = re.sub(r\"@\\w+\", \"\", text)\n",
    "    text = re.sub(r\"[^a-zA-Z\\s]\", \"\", text)\n",
    "\n",
    "    words = text.split()\n",
    "    words = [w for w in words if w not in stop_words]\n",
    "    words = [lemmatizer.lemmatize(w) for w in words]\n",
    "\n",
    "    return \" \".join(words)\n",
    "\n",
    "# UI\n",
    "st.title(\"✈️ Social Media Sentiment Analyzer\")\n",
    "\n",
    "text = st.text_area(\"Enter a social media post:\")\n",
    "\n",
    "if st.button(\"Analyze\"):\n",
    "    if text.strip() != \"\":\n",
    "        clean = preprocess(text)\n",
    "        vec = vectorizer.transform([clean])\n",
    "        pred = model.predict(vec)\n",
    "\n",
    "        sentiment = encoder.inverse_transform(pred)[0]\n",
    "\n",
    "        st.success(f\"Predicted Sentiment: {sentiment}\")\n",
    "    else:\n",
    "        st.warning(\"Please enter some text\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "632ecf33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting streamlitNote: you may need to restart the kernel to use updated packages.\n",
      "\n",
      "  Downloading streamlit-1.12.0-py2.py3-none-any.whl (9.1 MB)"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts."
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Collecting rich>=10.11.0\n",
      "  Downloading rich-15.0.0-py3-none-any.whl (310 kB)\n",
      "Collecting tzlocal>=1.1\n",
      "  Downloading tzlocal-5.3.1-py3-none-any.whl (18 kB)\n",
      "Requirement already satisfied: toml in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (0.10.2)\n",
      "Collecting blinker>=1.0.0\n",
      "  Downloading blinker-1.9.0-py3-none-any.whl (8.5 kB)\n",
      "Collecting cachetools>=4.0\n",
      "  Downloading cachetools-6.2.6-py3-none-any.whl (11 kB)\n",
      "Requirement already satisfied: pandas>=0.21.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (1.3.4)\n",
      "Requirement already satisfied: tornado>=5.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (6.1)\n",
      "Collecting validators>=0.2\n",
      "  Downloading validators-0.35.0-py3-none-any.whl (44 kB)\n",
      "Collecting pyarrow>=4.0\n",
      "  Downloading pyarrow-21.0.0-cp39-cp39-win_amd64.whl (26.2 MB)\n",
      "Collecting semver\n",
      "  Downloading semver-3.0.4-py3-none-any.whl (17 kB)\n",
      "Requirement already satisfied: watchdog in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (2.1.3)\n",
      "Requirement already satisfied: numpy in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (1.20.3)\n",
      "Collecting gitpython!=3.1.19\n",
      "  Downloading gitpython-3.1.49-py3-none-any.whl (212 kB)\n",
      "Collecting protobuf<4,>=3.12\n",
      "  Downloading protobuf-3.20.3-cp39-cp39-win_amd64.whl (904 kB)\n",
      "Collecting pympler>=0.9\n",
      "  Downloading Pympler-1.1-py3-none-any.whl (165 kB)\n",
      "Requirement already satisfied: importlib-metadata>=1.4 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (4.8.1)\n",
      "Requirement already satisfied: packaging>=14.1 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (21.0)\n",
      "Requirement already satisfied: typing-extensions>=3.10.0.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (3.10.0.2)\n",
      "Collecting altair>=3.2.0\n",
      "  Downloading altair-6.0.0-py3-none-any.whl (795 kB)\n",
      "Requirement already satisfied: pillow>=6.2.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (8.4.0)\n",
      "Collecting pydeck>=0.1.dev5\n",
      "  Downloading pydeck-0.9.2-py2.py3-none-any.whl (11.3 MB)\n",
      "Requirement already satisfied: requests>=2.4 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (2.26.0)\n",
      "Requirement already satisfied: python-dateutil in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (2.8.2)\n",
      "Requirement already satisfied: click>=7.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from streamlit) (8.0.3)\n",
      "Collecting typing-extensions>=3.10.0.0\n",
      "  Downloading typing_extensions-4.15.0-py3-none-any.whl (44 kB)\n",
      "Collecting narwhals>=1.27.1\n",
      "  Downloading narwhals-2.20.0-py3-none-any.whl (449 kB)\n",
      "Requirement already satisfied: jsonschema>=3.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (3.2.0)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from altair>=3.2.0->streamlit) (2.11.3)\n",
      "Requirement already satisfied: colorama in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from click>=7.0->streamlit) (0.4.4)\n",
      "Collecting gitdb<5,>=4.0.1\n",
      "  Downloading gitdb-4.0.12-py3-none-any.whl (62 kB)\n",
      "Collecting smmap<6,>=3.0.1\n",
      "  Downloading smmap-5.0.3-py3-none-any.whl (24 kB)\n",
      "Requirement already satisfied: zipp>=0.5 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from importlib-metadata>=1.4->streamlit) (3.6.0)\n",
      "Requirement already satisfied: pyrsistent>=0.14.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (0.18.0)\n",
      "Requirement already satisfied: six>=1.11.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (1.16.0)\n",
      "Requirement already satisfied: setuptools in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (58.0.4)\n",
      "Requirement already satisfied: attrs>=17.4.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from jsonschema>=3.0->altair>=3.2.0->streamlit) (21.2.0)\n",
      "Requirement already satisfied: pyparsing>=2.0.2 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from packaging>=14.1->streamlit) (3.0.4)\n",
      "Requirement already satisfied: pytz>=2017.3 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from pandas>=0.21.0->streamlit) (2021.3)\n",
      "Requirement already satisfied: MarkupSafe>=0.23 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from jinja2->altair>=3.2.0->streamlit) (1.1.1)\n",
      "Requirement already satisfied: pywin32>=226 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from pympler>=0.9->streamlit) (228)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2021.10.8)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (3.2)\n",
      "Requirement already satisfied: charset-normalizer~=2.0.0 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (2.0.4)\n",
      "Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\\users\\nilanjan chanda\\anaconda3\\lib\\site-packages (from requests>=2.4->streamlit) (1.26.7)\n",
      "Collecting pygments<3.0.0,>=2.13.0\n",
      "  Downloading pygments-2.20.0-py3-none-any.whl (1.2 MB)\n",
      "Collecting markdown-it-py>=2.2.0\n",
      "  Downloading markdown_it_py-3.0.0-py3-none-any.whl (87 kB)\n",
      "Collecting mdurl~=0.1\n",
      "  Downloading mdurl-0.1.2-py3-none-any.whl (10.0 kB)\n",
      "Collecting tzdata\n",
      "  Downloading tzdata-2026.2-py2.py3-none-any.whl (349 kB)\n",
      "Installing collected packages: smmap, mdurl, tzdata, typing-extensions, pygments, narwhals, markdown-it-py, gitdb, validators, tzlocal, semver, rich, pympler, pydeck, pyarrow, protobuf, gitpython, cachetools, blinker, altair, streamlit\n",
      "  Attempting uninstall: typing-extensions\n",
      "    Found existing installation: typing-extensions 3.10.0.2\n",
      "    Uninstalling typing-extensions-3.10.0.2:\n",
      "      Successfully uninstalled typing-extensions-3.10.0.2\n",
      "  Attempting uninstall: pygments\n",
      "    Found existing installation: Pygments 2.10.0\n",
      "    Uninstalling Pygments-2.10.0:\n",
      "      Successfully uninstalled Pygments-2.10.0\n",
      "Successfully installed altair-6.0.0 blinker-1.9.0 cachetools-6.2.6 gitdb-4.0.12 gitpython-3.1.49 markdown-it-py-3.0.0 mdurl-0.1.2 narwhals-2.20.0 protobuf-3.20.3 pyarrow-21.0.0 pydeck-0.9.2 pygments-2.20.0 pympler-1.1 rich-15.0.0 semver-3.0.4 smmap-5.0.3 streamlit-1.12.0 typing-extensions-4.15.0 tzdata-2026.2 tzlocal-5.3.1 validators-0.35.0\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "\n",
      "spyder 5.1.5 requires pyqt5<5.13, which is not installed.\n",
      "spyder 5.1.5 requires pyqtwebengine<5.13, which is not installed.\n"
     ]
    }
   ],
   "source": [
    "pip install streamlit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39eccc2b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
