# wav2vec-toolkit
A collection of scripts to preprocess ASR datasets and finetune language-specific Wav2Vec2 XLSR models

This repository accompanies the 🤗 HuggingFace Community Paper on finetuning Wav2Vec2 XLSR for 
low-resource languages **[link]**

# How to contribute
(Mostly identical to the [huggingface/datasets contributing guide](https://raw.githubusercontent.com/huggingface/datasets/master/CONTRIBUTING.md))

1. Fork the [repository](https://github.com/anton-l/wav2vec-toolkit) by clicking on the 'Fork' button on the repository's page. This creates a copy of the code under your GitHub user account.

2. Clone your fork to your local disk, and add the base repository as a remote:

	```bash
	git clone git@github.com:<your Github handle>/wav2vec-toolkit.git
	cd wav2vec-toolkit
	git remote add upstream https://github.com/anton-l/wav2vec-toolkit.git
	```

3. Set up a development environment by running the following command in a virtual environment:

	```bash
	conda create -n env python=3.7 --y
	conda activate env
	pip install -e ".[dev]"
	pip install -r languages/{YOUR_SPECIFIC_LANGUAGE}/requirements.txt
	```

   (If wav2vec-toolkit was already installed in the virtual environment, remove
   it with `pip uninstall wav2vec_toolkit` before reinstalling it in editable
   mode with the `-e` flag.)

3. Create a new branch to hold your development changes:

	```bash
	git checkout -b a-descriptive-name-for-my-changes
	```

	**do not** work on the `master` branch.

4. Develop the features on your branch.
   1. Adding a new language [here](ADD_NEW_LANGUAGE.md)

5. Format your code. Run black and isort so that your newly added files look nice with the following command:

	```bash
	black --line-length 119 --target-version py36 src scripts languages
	isort src scripts languages
	```

7. Once you're happy with your implementation, add your changes and make a commit to record your changes locally:

	```bash
	git add .
	git commit
	```

	It is a good idea to sync your copy of the code with the original
	repository regularly. This way you can quickly account for changes:

	```bash
	git fetch upstream
	git rebase upstream/main
    ```

   Push the changes to your account using:

   ```bash
   git push -u origin a-descriptive-name-for-my-changes
   ```

8. Once you are satisfied, go the webpage of your fork on GitHub. Click on "Pull request" to send your to the project maintainers for review.
