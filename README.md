# Research-the-Performance-Test-Model-for-Machine-Learning-Intrusion-Detection-Dystem-
Presents the results of the research performance test software for capsule, convolutional and generative-adversarial networks as part of intrusion detection system.
Configure
I. Create GCE 
Creates an 8xV100 instance with 4 nvme drives. Output of the command will provide the command to run to SSH to the machine. 
python perfzero/lib/cloud_manager.py create --accelerator_count 8 --nvme_count 4
II. Build docker on GCE 
After logging into the instance run the following command to create a docker instance with the latest nightly TF 2.0 build. 
python3 perfzero/lib/setup.py --dockerfile_path=docker/Dockerfile_ubuntu_20.04_tf_v2
III. Start and "enter" the docker 
nvidia-docker run -it --rm -v $(pwd):/workspace -v /data:/data perfzero/tensorflow bash
IV. Run tests
python3 /workspace/perfzero/lib/benchmark.py \
--git_repos="https://github.com/tensorflow/models.git;benchmark" \
--python_path=models \
--data_downloads="gs://tf-perf-imagenet-uswest1/tensorflow/cifar10_data/cifar-10-batches-bin" \
--benchmark_methods=official.benchmark.keras_cifar_benchmark.Resnet56KerasBenchmarkReal.benchmark_1_gpu_no_dist_strat
V. Delete the instance when done
python perfzero/lib/cloud_manager.py delete
