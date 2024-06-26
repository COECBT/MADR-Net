# -*- coding: utf-8 -*-
"""losses.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h4RfXjbOuAM3wGtDJ1O101rYTiqDuk_m
"""

from keras_unet_collection import losses

def hybrid_loss(y_true, y_pred):

    loss_focal = losses.focal_tversky(y_true, y_pred, alpha=0.5, gamma=4/3)
    loss_iou = losses.iou_seg(y_true, y_pred)

    # (x)
    loss_dice = losses.dice(y_true, y_pred)

    return loss_focal+loss_iou +loss_dice