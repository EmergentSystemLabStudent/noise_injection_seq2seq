#python -m nmt.nmt \
#--out_dir=./Models/ex2/rho=0.05 \
#--inference_input_file=./speech_recognition_results/speaker_T/sphinx_phonemeresultdata.csv \
#--inference_output_file=./Results/ex2/rho=0.05/speaker_T/sphinx


python -m nmt.nmt \
--out_dir=./Models/ex1/rho=0.1 \
--inference_input_file=./speech_recognition_results/speaker_K/google_phonemeresultdata.csv \
--inference_output_file=./Results/ex1/rho=0.1_1/speaker_K/google

python -m nmt.nmt \
--out_dir=./Models/ex1/rho=0.1 \
--inference_input_file=./speech_recognition_results/speaker_L/google_phonemeresultdata.csv \
--inference_output_file=./Results/ex1/rho=0.1_1/speaker_L/google

python -m nmt.nmt \
--out_dir=./Models/ex1/rho=0.1 \
--inference_input_file=./speech_recognition_results/speaker_T/google_phonemeresultdata.csv \
--inference_output_file=./Results/ex1/rho=0.1_1/speaker_T/google

python -m nmt.nmt \
--out_dir=./Models/ex1/rho=0.1 \
--inference_input_file=./speech_recognition_results/speaker_W/google_phonemeresultdata.csv \
--inference_output_file=./Results/ex1/rho=0.1_1/speaker_W/google

#python -m nmt.nmt \
#--out_dir=./Models/ex2/rho=0.15 \
#--inference_input_file=./speech_recognition_results/speaker_T/sphinx_phonemeresultdata.csv \
#--inference_output_file=./Results/ex2/rho=0.15/speaker_T/sphinx

#python -m nmt.nmt \
#--out_dir=./Models/ex2/rho=0.2 \
#--inference_input_file=./speech_recognition_results/speaker_T/sphinx_phonemeresultdata.csv \
#--inference_output_file=./Results/ex2/rho=0.2/speaker_T/sphinx

#python -m nmt.nmt \
#--out_dir=./Models/ex2/rho=0.25 \
#--inference_input_file=./speech_recognition_results/speaker_T/sphinx_phonemeresultdata.csv \
#--inference_output_file=./Results/ex2/rho=0.25/speaker_T/sphinx

#python -m nmt.nmt \
#--out_dir=./Models/ex2/rho=0.3 \
#--inference_input_file=./speech_recognition_results/speaker_T/sphinx_phonemeresultdata.csv \
#--inference_output_file=./Results/ex2/rho=0.3/speaker_T/sphinx






