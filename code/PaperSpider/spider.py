from config import opt
import spidersMoudle


def spider(**kwargs):
    opt.parse(kwargs)
    spiderTool = getattr(spidersMoudle, opt.spiderTool)(opt)
    spiderTool.main()


if __name__ == '__main__':
    import fire
    fire.Fire()

