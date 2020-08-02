all:
	@echo "测试中"

install:
	#[[ -f ${HOME}/bin ]] && cp /script/* ${HOME}/bin
	#cp -p ./script/* ${HOME}/bin
	for i in ./script/*; do echo ${i}; echo ${i%%.*}; cp -pv ${i} ${HOME}/bin/${i%%.*}; chmod 755 ${HOME}/bin/${i%%.*}; done
	#chmod 755 ${HOME}/bin/*
