pretrained = "/home/s/tuyenld/mae_continue_pretrain_with_register/weight/last.pth"
# pretrained = "/workspace/mae/pretrain/runs/pretrainv2/continue_pretrain3/weight/epoch_90.pth"
model = dict(
    type='EncoderDecoderRaBiT',
    pretrained=pretrained,
    backbone=dict(
        type='MaskedAutoencoderViT',
        downstream_size=384,
        num_register_tokens=4,
        # num_register_tokens=0,
        out_indices=(2, 5, 8, 11),
    ),
    neck=dict(type='Feature2Pyramid', embed_dim=768, rescales=[4, 2, 1, 0.5]),
    decode_head=None,
    train_cfg=dict(),
    test_cfg=dict(mode='whole')
)
