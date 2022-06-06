module.exports = {
  deploy : {
    development : {
      user : 'neko',
      host : '172.16.2.97',
      ref  : 'origin/tuanna',
      repo : 'git@git.vmo.dev:global/vmo-devops-internal/fresher-project/tuanna4-project.git',
      path : '/home/neko/flask',
      'post-setup' : 'pip3 install -r requirements.txt; pm2 start ecosystem_run.json',
      'post-deploy' : 'pm2 restart ecosystem_run.json'
    }
  }
};