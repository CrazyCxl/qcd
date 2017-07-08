qcd ()
{
    QD=~/.qcd/tmp_dir
	export QD
	/usr/bin/qcd.py "$@"
	[ ! `cat $QD` ] || cd "`cat $QD`"
	rm -f "$QD"
        unset QD;
}
