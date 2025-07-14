# AWS S3 + Route 53 Static Website Hosting Lab

This project demonstrates how to host a fully functional static website using **Amazon S3** and make it accessible with a **custom domain via Route 53**.

##  Technologies Used
- Amazon S3 (Simple Storage Service)
- Amazon Route 53 (DNS)
- HTML (Static web content)

##  Folder Structure

s3-static-site/

├── index.html

├── error.html

└── README.md


## Steps Completed

1. **Created an S3 Bucket**
   - Named exactly as the domain: `yourdomain.com`
   - Disabled public access block

2. **Uploaded HTML Files**
   - `index.html`: Main landing page
   - `error.html`: Custom error page

3. **Enabled Static Website Hosting**
   - Configured index and error documents in bucket settings

4. **Set Public Read Bucket Policy**
   ```json
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Sid": "PublicReadGetObject",
         "Effect": "Allow",
         "Principal": "*",
         "Action": "s3:GetObject",
         "Resource": "arn:aws:s3:::addisonengineer.org/*"
       }
     ]
   }
# aws-s3-route53-static-site
