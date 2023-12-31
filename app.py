import os
os.chdir(f"/home/xlab-app-center")
os.system(f"git clone -b v2.5 https://github.com/camenduru/stable-diffusion-webui /home/xlab-app-center/stable-diffusion-webui")
os.chdir(f"/home/xlab-app-center/stable-diffusion-webui")
os.system(f"git lfs install")
os.system(f"git reset --hard")
os.system(f"sed -i -e '/demo:/r /home/xlab-app-center/header.py' /home/xlab-app-center/stable-diffusion-webui/modules/ui.py")
os.system(f"sed -i -e '253,258d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '186,228d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '171,178d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '108,113d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_settings.py")
os.system(f"sed -i -e '208,210d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_loadsave.py")
os.system(f"sed -i -e '197,200d' /home/xlab-app-center/stable-diffusion-webui/modules/ui_loadsave.py")
os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/sdxl-base-1.0/weight//sd_xl_base_1.0.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o sd_xl_base_1.0.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/sdxl-refiner-1.0/weight//sd_xl_refiner_1.0.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o sd_xl_refiner_1.0.safetensors")
# os.system(f"aria2c --console-log-level=error -c -x 16 -s 16 -k 1M https://download.openxlab.org.cn/models/camenduru/cyber-realistic/weight//cyberrealistic_v32.safetensors -d /home/xlab-app-center/stable-diffusion-webui/models/Stable-diffusion -o cyberrealistic_v32.safetensors")
os.system(f"python launch.py --cors-allow-origins=* --xformers --enable-insecure-extension-access --theme dark --gradio-queue --disable-safe-unpickle --ui-settings-file /home/xlab-app-center/config.json --ui-config-file /home/xlab-app-center/ui-config.json")
