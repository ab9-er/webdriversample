from selenium import webdriver
import argparse


def main(link_name):
    f = webdriver.Firefox()
    f.get("https://the-internet.herokuapp.com")
    try:
        link = f.find_element_by_link_text(link_name)
        link.click()
    except:
        print("Link's name not found")
    finally:
        f.quit()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Link name')
    parser.add_argument('link_name', nargs='?')
    args = parser.parse_args()
    main(args.link_name)