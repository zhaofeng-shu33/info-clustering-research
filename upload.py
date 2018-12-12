import os
import oss2

if __name__ == '__main__':
    os.chdir('build')
    access_key_id = os.getenv('AccessKeyId')
    access_key_secret = os.getenv('AccessKeySecret')
    auth = oss2.Auth(access_key_id, access_key_secret)
    bucket = oss2.Bucket(auth, 'http://oss-cn-shenzhen.aliyuncs.com', 'programmierung')
    # open `main.pdf` and `clustering.pdf` and upload them to the oss server
    main_pdf = open('main.pdf')
    clustering_pdf = open('clustering.pdf')
    research_base = 'research/info-clustering/'
    bucket.put_object(research_base + 'main.pdf', main_pdf)
    bucket.put_object(research_base + 'clustering.pdf', clustering_pdf)    