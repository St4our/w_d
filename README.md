Дополнительно: 
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

1. Установить ROCm
AMD использует ROCm (Radeon Open Compute) вместо CUDA. Для RX 6800 подойдет версия ROCm 5.x. Установите её следующим образом:

bash
Копировать
Редактировать
sudo apt update && sudo apt upgrade -y
sudo apt install -y rocm-hip-libraries rocm-hip-runtime hipblas hipsparse miopen-hip
echo 'export PATH=/opt/rocm/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/opt/rocm/lib:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc
Проверьте установку:

bash
Копировать
Редактировать
rocminfo
hipcc --version
2. Установить PyTorch с поддержкой ROCm
AMD предоставляет PyTorch с HIP/ROCm вместо CUDA. Установите его:

bash
Копировать
Редактировать
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm5.4
Проверьте, что PyTorch видит вашу видеокарту:

python
Копировать
Редактировать
import torch
print(torch.cuda.is_available())  # Должно быть True
print(torch.cuda.get_device_name(0))  # Должно вывести RX 6800
3. Установить transformers и accelerate
Hugging Face поддерживает ROCm через bitsandbytes и accelerate:

bash
Копировать
Редактировать
pip install transformers accelerate bitsandbytes
4. Настроить accelerate для AMD GPU
Запустите команду:

bash
Копировать
Редактировать
accelerate config
Выберите параметры:

Compute Device: ROCm
Distributed Training: No
FP16: Yes (если ваша карта поддерживает)
5. Изменить код для работы с ROCm
Добавьте параметр torch_dtype=torch.float16 и явно укажите device="cuda":

python
Копировать
Редактировать
pipe = pipeline("text-generation", model="amd/Instella-3B-Instruct", 
                torch_dtype=torch.float16, device=0)
6. Запустить код
Теперь можно запустить ваш код:

bash
Копировать
Редактировать
python script.py
