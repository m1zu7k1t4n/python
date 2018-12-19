# coding: utf-8
import sys
import requests
import pyperclip

argvs = sys.argv
argc = len(argvs)
data = """Abstract
Recently developed Structure from Motion (SfM) reconstruction
approaches enable the creation of large scale 3D
models of urban scenes. These compact scene representations
can then be used for accurate image-based localization,
creating the need for localization approaches that are
able to efficiently handle such large amounts of data. An
important bottleneck is the computation of 2D-to-3D correspondences
required for pose estimation. Current stateof-the-art
approaches use indirect matching techniques to
accelerate this search. In this paper we demonstrate that
direct 2D-to-3D matching methods have a considerable
potential for improving registration performance. We derive
a direct matching framework based on visual vocabulary
quantization and a prioritized correspondence search.
Through extensive experiments, we show that our framework
efficiently handles large datasets and outperforms current
state-of-the-art methods.
1. Introduction
Image-based localization is an important problem in
computer vision. Its applications include localization and
navigation for both pedestrians [22, 31, 13] and robots
[6, 5], Augmented Reality [1, 3], and the visualization of
photo collections [26]. Image-based localization is also an
important part in the pipeline of higher-level computer vision
tasks such as semantic object annotation [9] and can
be used as an initial pose estimate to speed up large-scale
reconstructions from Internet photo collections [27].
Traditionally, large-scale image-based localization has
been treated as an image retrieval problem. After finding
those images in a database that are most similar to the query
image, the location of the query can be determined relative
to them [22, 31]. The huge progress achieved in the field
of image retrieval enables the use of an increasing number
of images for the representation of real world scenes
[25, 19, 20]. However, the localization accuracy obtained
this way cannot be better than the precision of the GPS
positions available for the database images. To achieve a
higher localization accuracy, more detailed information is
needed which can be obtained from a 3D reconstruction
of the scene. Using these models additionally permits to"""
data = data.replace("\n","")

url = "https://translate.google.com/translate_a/single"

headers = {
    "Host": "translate.google.com",
    "Accept": "*/*",
    "Cookie": "",
    "User-Agent": "GoogleTranslate/5.9.59004 (iPhone; iOS 10.2; ja; iPhone9,1)",
    "Accept-Language": "ja-jp",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
    }

sentence = " ".join(argvs[1:])

params = {
    "client": "it",
    "dt": ["t", "rmt", "bd", "rms", "qca", "ss", "md", "ld", "ex"],
    "otf": "2",
    "dj": "1",
    "q": data,
    "hl": "ja",
    "ie": "UTF-8",
    "oe": "UTF-8",
    "sl": "en",
    "tl": "ja",
    }




res = requests.get(
    url=url,
    headers=headers,
    params=params,
    )

res = res.json()
print(res["sentences"][0]["trans"])


