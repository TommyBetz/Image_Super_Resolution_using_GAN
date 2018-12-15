## Image Super-Resolution Using GANs

To run this project

* Training

```bash
pyhon main_ssim.py
```
Place the trained models inside checkpoint directory.

> Requirements: Tensorflow, Tensorlayer, easydict

* Testing
The generated images will be created inside a samples directory.
```bash
python main_ssim.py --mode=evaluate
```
* References
  * [Photo-Realistic Single Image Super-Resolution Using a Generative Adversarial Network](https://arxiv.org/abs/1609.04802)
  * [Github](https://github.com/tensorlayer/srgan)
  * [VGG 19 Model](https://mega.nz/#!xZ8glS6J!MAnE91ND_WyfZ_8mvkuSa2YcA7q-1ehfSm-Q1fxOvvs)
  * [DIV2K Dataset](https://data.vision.ee.ethz.ch/cvl/DIV2K/)
  > The models must be placed in the root directory of the project.
