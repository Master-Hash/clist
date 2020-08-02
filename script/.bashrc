fuck ()
{
    local $(grep --color=never "PKGDIR=.*" /etc/portage/make.conf);
    echo $PKGDIR
}

upload ()
{
    git add .
    git commit -m "Auto upload"
    git push --all
}
