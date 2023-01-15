import unittest
import os
import subprocess
from shutil import rmtree, copytree
from obsidian_to_hugo import ObsidianToHugo

class CLITestCase(unittest.TestCase):
    def setUp(self) -> None:
      """
      Duplicate ./mocks and all its contents into ./temp 
      """
      if os.path.exists("./tests/temp"):
        rmtree("./tests/temp")
      copytree("./tests/mocks", "./tests/temp")

    # def tearDown(self) -> None:
    #   """
    #   Remove ./temp
    #   """
    #   rmtree("./tests/temp")
    
    def test_copy(self):
      """
      Files inside ./temp/hugo should be the same as ./temp/obsidian
      ignoring .obsidian directory
      """
      subprocess.run("python3 -m obsidian_to_hugo --obsidian-vault-dir=./tests/temp/obsidian --hugo-content-dir=./tests/temp/hugo", shell=True)
      obsidian_files = os.listdir("./tests/temp/obsidian") 
      obsidian_files.remove(".obsidian")
      hugo_files = os.listdir("./tests/temp/hugo")
      self.assertEqual(obsidian_files, hugo_files)
    
    def test_custom_processor(self):
      """
      Instantiate with custom processor function and test it 
      """
      def custom_processor(text: str) -> str:
        return text.replace("abc", "xyz")
      
      obsidian_to_hugo = ObsidianToHugo(
        obsidian_vault_dir="./tests/temp/obsidian",
        hugo_content_dir="./tests/temp/hugo",
        processors=[custom_processor]
      )

      # create a file with abc in it
      with open("./tests/temp/obsidian/test.md", "w") as f:
        f.write("abc")

      obsidian_to_hugo.run()

      with open("./tests/temp/hugo/test.md", "r") as f:
        self.assertEqual(f.read(), "xyz")
